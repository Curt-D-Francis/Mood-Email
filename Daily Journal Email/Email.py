import mysql.connector
from customtkinter import *
import requests
#Set up EasyCron API
headers = {"token" : "2bbb78349ce0d5ca8f18f5721977ef61", "method" : "enable"}
Enable_api_url = f"https://www.easycron.com/rest/enable?token={headers['token']}&id=7467181"
EnableCron = requests.get(Enable_api_url, headers=headers)
#Establish connection to database
Mood_DB = mysql.connector.connect(
    host = "localhost",
    
    user = "root",

    password = "Number1jr!",

    database = "moodemail"
)
# Create cursor to navigate database
DB_cursor = Mood_DB.cursor()

#Establish CustomTK
app = CTk()
app.geometry("750x550")
set_appearance_mode("dark")
frame = CTkFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
frame.pack(expand=True)
Moodvalue = []
#Define What happens in Button click.
def Btnclick():
    mood_value = IndividualMood.get()
    Moodvalue.append(mood_value.strip('"'))
    try:
        #Establish repeated query and assign mood_value to data
        query = "INSERT INTO moods (Mood) VALUES (%s)"
        data = (mood_value,)
        DB_cursor.execute(query,data)
        #Commit to Database
        Mood_DB.commit()
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        app.destroy()
#Configure Columns
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
#Labels
MoodLabel = CTkLabel(master=app, text="Whats your Mood Today?", font=("Arial", 22))
MoodLabel.place(relx=0.5,rely=0, anchor="n")
#TextBox
IndividualMood = CTkComboBox(master=frame, values=["Sad", "Happy", "Neutral", "Angry"])
IndividualMood.place(relx=0.5, rely=0.5, anchor="center")
#Submit Button
submitbtn = CTkButton(master=frame, text= "Submit", corner_radius=32, fg_color="#FFCC70", hover_color="#4158D0", border_color="#FFCC70", border_spacing=2, command=Btnclick)
submitbtn.place(relx=0.5, rely=0.75, anchor="s")



app.mainloop()

