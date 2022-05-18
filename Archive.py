import sqlite3 as sql 
#isma jwa alcode sql kan fik tsmia betnjan kman
import os.path as path 


DATABASE_FILE_PATH = './data.db'
#finding database if it doesn't exist this will creates it
#panada to read to csv 
if not path.isfile(DATABASE_FILE_PATH):
    print('Database does not exists, creating ... ')
    connection = sql.connect(DATABASE_FILE_PATH)
    cursor = connection.cursor() 
    #data moduling
    """

    first_name 15 
    middle_name 15 
    last_name 15 

    date_of_birth DATE
    residence 50
    status 25 
    notes 500

    """
    #archive is the name of the table
    #each comma mean a new coloum 
    #Autoincrement adds a new id itself ma bt3bi elfara3'
    #take a photo form a other table with the forgeign key
    
    cursor.execute(""" 
        CREATE TABLE archive(
            id INTEGER NOT NULL ,
            First_Name                          varchar(15),
            Middle_Name                         varchar(15),
            Last_Name                           varchar(15),
            Date_of_Birth                       DATE,
            Status                              varchar (50),
            Residence                           varchar (50),
            Notes                               varchar (500),
            Image_Name                          varchar (15),
            PRIMARY KEY(id) 


            --image_id                            INT
       e 
            --FOREIGN KEY(image_id) REFERENCES Image(id)




        )
   
    
    """)


    cursor.execute()
#commit is for saving the changes
    connection.commit()
    connection.close()

else : 
    print("Database exists")

connection = sql.connect(DATABASE_FILE_PATH)
cursor = connection.cursor() 
cursor.execute(""" SELECT * FROM archive;""")

for row in cursor:
    print(row)



#USER INTERFACE NOW 


import tkinter as tk 
#Tk make me a window
HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("Archive")

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
# DON'T FORGET THE # BEFORE THE COLOOOOOR!!

background_image = tk.PhotoImage(file ="ezgif-4-c7bcc3f7701c.gif")
#./ means that the image is in the same dirc
# python don't support jpg because it is stupid gif on the other hand is ok
background_label = tk.Label(root, image = background_image)
background_label.pack(fill = "both", expand = "yes")


frame = tk.Frame(root, bg = '#41B3A3',bd =5)
#bd = stands for border
frame.place(relx = 0.5,rely = 0.1, relwidth = 0.75 , relheight = 0.1, anchor = 'n')
# relwidth how much of the wedget will be fulfill with the color.
# relx and rely are used here to center the color 
# anchor is not nice
  
entry = tk.Entry(frame,font=40)
#font is the size of the font
entry.place(relwidth=0.65, relheight = 1 )
# the whole screen is relwidth =1 and relheight = 1 

button = tk.Button(frame,bg = '#2F2FA2', fg = "white", text = "Search",font = 40 ,  command=lambda: test_function(entry.get()))
button.place(relx=0.7, relheight =1, relwidth = 0.3 )

lower_frame = tk.Frame(root, bg='#41B3A3', bd=2)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)






#Label text is class (piece) and its name in lib is label
# w is of-type label and label is class in the lib to display a text



def on_click_quit():
    exit()



def show():
    cursor.execute("SELECT * FROM archive ;")
    string_to_display = str(cursor.fetchall()) # for loop is for bringing specfic items
    background_label.config(text = string_to_display)

#commad is an assigment to function that will be commanded
but2 = tk.Button(root, text="Show", bg ='#2F2FA2', fg = 'white', command = show)
#pack to make in the screen
but2.pack()

but2.place(x = 220 , y = 220)
def test_function(entry):
    print("this is the entry: ", entry)



#root is sustain viewing for the window IT MUST BE BY THE END OF THE ENDS
root.mainloop()

