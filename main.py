import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

data=pd.read_csv("data.csv")
#filling missing values
data['ShortPassing'].fillna(data['ShortPassing'].mean(), inplace = True)
data['Volleys'].fillna(data['Volleys'].mean(), inplace = True)
data['Dribbling'].fillna(data['Dribbling'].mean(), inplace = True)
data['Curve'].fillna(data['Curve'].mean(), inplace = True)
data['FKAccuracy'].fillna(data['FKAccuracy'], inplace = True)
data['LongPassing'].fillna(data['LongPassing'].mean(), inplace = True)
data['BallControl'].fillna(data['BallControl'].mean(), inplace = True)
data['HeadingAccuracy'].fillna(data['HeadingAccuracy'].mean(), inplace = True)
data['Finishing'].fillna(data['Finishing'].mean(), inplace = True)
data['Crossing'].fillna(data['Crossing'].mean(), inplace = True)
data['Weight'].fillna('200lbs', inplace = True)
data['Contract Valid Until'].fillna(2019, inplace = True)
data['Height'].fillna("5'11", inplace = True)
data['Loaned From'].fillna('None', inplace = True)
data['Joined'].fillna('Jul 1, 2018', inplace = True)
data['Jersey Number'].fillna(8, inplace = True)
data['Body Type'].fillna('Normal', inplace = True)
data['Position'].fillna('ST', inplace = True)
data['Club'].fillna('No Club', inplace = True)
data['Work Rate'].fillna('Medium/ Medium', inplace = True)
data['Skill Moves'].fillna(data['Skill Moves'].median(), inplace = True)
data['Weak Foot'].fillna(3, inplace = True)
data['Preferred Foot'].fillna('Right', inplace = True)
data['International Reputation'].fillna(1, inplace = True)
data['Wage'].fillna('€200K', inplace = True)
data.fillna(0, inplace = True)
#Since this data contains specific positions of each players like ST,RCM,LF,DCM etc...
#it may be difficult to understand position for a new person who don't know much about all positions in game.
#So let's just create a new position category which divide each players position into 4 categories--
#defender
#* goalkeeper
#* midfielder
# forward
list_for= ['ST','LW','RW','LS','RS','CF','RF','LF']
list_back= ['CB','LB','RB','LCB','RCB','RWB','LWB']
def new_pos(value):
    if(value=='GK'):
        return 'goalkeeper'
    if(value in list_for):
        return 'forward'
    if(value in list_back):
        return 'defender'
    else:
        return 'midfielder'


data['new_position'] = data['Position'].apply(lambda x : new_pos(x))

option=st.sidebar.selectbox("What yo want to explore-->",["HomePage","Visualizations","Comparisions","Game"])
if(option=="HomePage"):
    st.title("FIFA19 Analysis(Pictures Telling Stories)")
    st.text("FIFA 19 is a football simulation video game developed by EA Vancouver as part of Electronic Arts' FIFA series.")
    st.markdown("In this web app we'll cover Data preparation,Exploratory Analysis of data ,Data Visualizations and comparisions between atrributes of our Data.We'll use Python Language for all the visualization and exploration Part.")
    st.image("img1.png")

    st.write("We use FIFA19 dataset present in Kaggle for our Analysis")
    st.subheader("To show the size of our data press the below Buttton:")
    if st.button("show size of data"):#for button
        df=data.shape;
        st.write("The size of data is:",df[0]," rows and ",df[1]," columns")

    st.subheader("To see the small sample of our data:")
    if st.checkbox("Show Raw Data",False):#for checkbox
        st.subheader("Raw Data")
        st.write(data.head(100))
    st.subheader("Let's Check our data contains Null Values or not")
    st.write(data.isnull().sum())
    st.markdown("We can see that our data is free of null values")

    st.header("What To Explore??")
    st.markdown("You can choose other options from the sidebar to explore more things.This web app contains 3 main segments:")
    st.markdown("1.Visualization:This portion contains variours charts and graphs of Different attributes of players")
    st.markdown("2.Comparisions:In this portion we ask some questions from the dataset and visualize all the results.")
    st.markdown("3.Game:This portion contains a intersting game to check your Luck.")
    st.image("img9.jpg")
    st.write("So without wasting any time,start your exploration")
if(option=="Visualizations"):
    st.title("Now let's see some charts and graphs to understand the data better:")
    st.image("img3.jpg")

    st.subheader("⚽ Comparision of Left Vs Right footed Players--")
    sns.countplot(data['Preferred Foot'],palette='Spectral');
    plt.title('Number of players of each Preferred Foot');
    st.pyplot(use_container_width=True)#used to view charts

    st.subheader("⚽ Comaparision of players among different positions featured in FIFA19--")
    sns.countplot('Position', data = data)
    plt.xticks(rotation=70)
    plt.title(label = 'Comparison of Positions and Players')
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Count of players in each category--")
    sns.countplot(data['new_position'],palette='bone');
    plt.title('Number of players of each category');
    st.pyplot(use_container_width=True)

    def convert(value):
        out = value.replace('lbs', '')
        return float(out)*0.453592
    data['Weight'] = data['Weight'].apply(lambda x : convert(x))

    st.subheader("⚽ Distribution of Weight Among Players in FIFA19")
    plt.style.use('tableau-colorblind10')
    sns.distplot(data['Weight'], color = 'blue')
    plt.title('Different Weights of the Players featuring in FIFA 2019', fontsize = 20)
    plt.xlabel('Weight associated with the players(in kgs)', fontsize = 16)
    plt.ylabel('count of Players', fontsize = 16)
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Distribution of Height Among Players in FIFA19")
    plt.style.use('tableau-colorblind10')
    sns.countplot(data['Height'],palette='twilight')
    plt.title('Different Heights of the Players featuring in FIFA 2019', fontsize = 20)
    plt.xlabel('Height associated with the player', fontsize = 16)
    plt.ylabel('count of Players', fontsize = 16)
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Top 20 countries with maximum players featured in FIFA19")
    data['Nationality'].value_counts().head(20).plot.bar();
    plt.title("Top 20 countries with maximum players featured in FIFA19",fontsize=20);
    plt.xlabel("Countries");
    plt.ylabel("Number of Players");
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Distribution of age in Some Top Clubs")
    top_club_names = ( 'Juventus','FC Barcelona', 'Chelsea', 'Real Madrid', 'Manchester City')
    clubs = data.loc[data['Club'].isin(top_club_names) & data['Age']]
    sns.boxenplot(x="Club", y="Age", data=clubs,palette='coolwarm');
    plt.title(label='Age distribution in the top 5 clubs', fontsize=25)
    plt.xlabel('Clubs', fontsize=20)
    plt.ylabel('Age', fontsize=20);
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Distribution of age in Some Top Countries")
    countries_names = ('France', 'Brazil', 'Germany', 'Belgium', 'Spain', 'Croatia', 'Argentina', 'Portugal', 'England', 'Italy')
    countries = data.loc[data['Nationality'].isin(countries_names) & data['Age']]
    fig, ax = plt.subplots()
    ax = sns.boxenplot(x="Nationality", y="Age", data=countries)
    ax.set_title(label='Age distribution in countries', fontsize=25)
    plt.xlabel('Countries', fontsize=20)
    plt.ylabel('Age', fontsize=20)
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Distribution of Overall Rating in FIFA19")
    sns.set(style = "dark", palette = "deep", color_codes = True)
    x = data.Overall
    plt.style.use('ggplot')
    ax = sns.distplot(x,color = 'b')
    ax.set_xlabel(xlabel = "Player\'s Scores", fontsize = 16)
    ax.set_ylabel(ylabel = 'Number of players', fontsize = 16)
    ax.set_title(label = 'Histogram of players Overall Scores', fontsize = 20)
    st.pyplot(use_container_width=True)

    st.subheader("⚽ Player Features chart for each category of players")

    st.image("img4.png")

if(option=="Comparisions"):
    st.title("Asking Questions with Data??")
    st.markdown("In this page we'll ask various questions with our data , and try to solve them with the help of python functions and analysis we made earlier.")
    st.image("img5.jpg")
    count=st.slider("Count of Top players You want to See",0,25)#for sidebar slider
    if count!=0:
        df=data.head(count)[['Name','Club','Nationality','Position','Overall']]
        st.write(df)

    st.header("Top 10 players of which category you want to see??")
    res=st.selectbox("",["None","defender","forward","goalkeeper","midfielder"])#for select box
    def eval(res):
        if(res=="defender"):
            temp=data[data['new_position']=='defender'].head(10)[['Name','Club','Nationality','Position','Overall']]
            return temp
        if(res=="forward"):
            temp=data[data['new_position']=='forward'].head(10)[['Name','Club','Nationality','Position','Overall']]
            return temp
        if(res=="goalkeeper"):
            temp=data[data['new_position']=='goalkeeper'].head(10)[['Name','Club','Nationality','Position','Overall']]
            return temp
        if(res=="midfielder"):
            temp=data[data['new_position']=='midfielder'].head(10)[['Name','Club','Nationality','Position','Overall']]
            return temp
    st.write(eval(res))

    st.header("Let's Check Top players of your Favourite Club")
    st.markdown("Please Write official name of your Favourite Club(eg. Chelsea,Manchester City,Juventus etc..)")
    club=st.text_input(" ")
    def club_player(club):
        temp=data[data['Club'] ==club][['Name','Position','Overall','Potential','Release Clause','Nationality','Age','Wage']].head(10)
        return temp
    st.write(club_player(club))

    st.header("Let's Check Top players of your Favourite National Team")
    st.markdown("Please Write official name of your favourite National Team(eg. Portugal,Germany,France etc..)")
    nation=st.text_input("")
    def nation_player(nation):
        temp=data[data['Nationality'] ==nation][['Name','Position','Overall','Potential','Release Clause','Nationality','Age','Wage']].head(10)
        return temp
    st.write(nation_player(nation))

    skills = ['Overall', 'Potential', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties',
       'Marking', 'StandingTackle', 'SlidingTackle']

    st.header("Head to Head Comaparision between 2 players  👊👊 👊👊 👊👊 👊👊")
    players=data['Name']
    player1=st.selectbox("Select Player 1",["None","L. Messi","K. De Bruyne","Cristiano Ronaldo","A. Griezmann","M. Salah","G. Bale","E. Hazard","L. Suárez","R. Lewandowski"])
    player2=st.selectbox("Select Player 2",["None","Cristiano Ronaldo","K. De Bruyne","E. Hazard","L. Suárez","R. Lewandowski","A. Griezmann","M. Salah","G. Bale"])
    def cal(player1,player2):
        p1 = data.loc[data['Name'] == player1]
        p1 = pd.DataFrame(p1, columns = skills)
        p2 = data.loc[data['Name'] == player2]
        p2 = pd.DataFrame(p2, columns = skills)

        plt.figure(figsize=(16,7))
        sns.pointplot(data=p1,color='green')
        sns.pointplot(data=p2, color='red')
        plt.text(2,22,player1+'\n'+player2,color='green',fontsize = 25)
        plt.text(2,22,player2,color='red',fontsize = 25)
        plt.xticks(rotation=70)
        plt.xlabel('Skills', fontsize=20)
        plt.ylabel('Skill value', fontsize=20)
        plt.title(player1+' vs '+player2, fontsize = 25)
        plt.show();
        st.pyplot(use_container_width=True)
    if(player1!="None" and player2!="None"):
        cal(player1,player2)

    BestSquad_DF = data[['Name', 'Age', 'Overall', 'Potential', 'Position']]
    st.header("Create Your Dream Team By choosing your Favourite Formation 👉👉👉")
    def find_best_squad(position):
        BestSquad_DF_copy = BestSquad_DF.copy()
        BestSquad = []
        for i in position:
            BestSquad.append([i,BestSquad_DF_copy.loc[[BestSquad_DF_copy[BestSquad_DF_copy['Position'] == i]['Overall'].idxmax()]]['Name'].to_string(index = False), BestSquad_DF_copy[BestSquad_DF_copy['Position'] == i]['Overall'].max()])
            BestSquad_DF_copy.drop(BestSquad_DF_copy[BestSquad_DF_copy['Position'] == i]['Overall'].idxmax(), inplace = True)

        return pd.DataFrame(np.array(BestSquad).reshape(11,3), columns = ['Position', 'Player', 'Overall'])
    formation= st.selectbox("Choose your desired Foramtion-->",["None","4-3-3","4-2-1-3","4-2-1-2-1","3-2-3-2","4-5-1","3-2-2-3"])
    def get_squad(formation):
        if formation=="4-3-3":
            return ['GK', 'LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'CM', 'RF', 'ST', 'LW']
        if formation=="4-2-1-3":
            return ['GK', 'LB', 'CB', 'CB', 'RB', 'CM', 'CM', 'CAM', 'RF', 'ST', 'LW']
        if formation=="4-2-1-2-1":
            return ['GK', 'LB', 'CB', 'CB', 'RB', 'RCM', 'LCM', 'CAM', 'RF', 'ST', 'LW']
        if formation=="3-2-3-2":
            return ['GK', 'CB', 'CB','CB' ,'LCB', 'RCB', 'RCM', 'LCM','CAM', 'ST', 'ST']
        if formation=="4-5-1":
            return ['GK', 'LB', 'CB', 'CB', 'RB', 'CAM', 'CAM', 'RCM', 'LCM', 'CDM', 'ST']
        if formation=="3-2-2-3":
            return ['GK', 'LB', 'CB', 'CB', 'RB', 'CDM', 'CDM', 'CAM', 'CAM', 'ST', 'LF']
        else:
            return "None"
    squad=get_squad(formation)
    if(squad!="None"):
        temp=find_best_squad(squad)
        st.write(temp)
if(option=="Game"):
    st.title("A Game of Luck")
    st.image("img6.jpg")
    st.write("Let's play a very interesting game and test your luck.In this game you need to choose any number of your choice any number for the computer,then system compares players based on your choice of selection totally randomly and then compares various attributes of players and give the results that who get the better card of player You or The Computer.")
    n1=st.slider("Number For You",0,2000)
    n2=st.slider("Number For Computer",0,2000)
    def game(n1,n2):
        n1=n1*np.random.rand(1)*10000*np.random.rand(1)
        n2=n2*np.random.rand(1)*10000*np.random.rand(1)
        n1=n1%2342
        n2=n2%2342
        if(n1>n2):
            st.success("You Won")
            st.image("img7.jpg")
        else:
            st.text("You Lose")
            st.image("img8.jpg")
        st.write("Thanks for Playing.Try different Values to check How Lucky You Are!!")

    game(n1,n2)
