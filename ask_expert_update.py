"""Ask The Expert

Hacks and Tweaks

Use different type of data
User input
    if the user forgets to capitalize, capitalize it for them
Fact check
    currently your program can't check if a new capital is correct. check with csv file to see if its correct, then add to text file

"""
from tkinter import Tk, simpledialog, messagebox
import csv
#simpledialog and messagebox are modules that will display the program

print('Ask the Expert - Capital Cities of the World')
root = Tk() #create an empty Tkinter window
root.withdraw() #hide the tkinter window

#Now setup a dictionary: LEsson on dictionaries. Their relationship to lists
the_world = {}


#function to scrub and read data from text file
def read_from_file():
    temp_list = []
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n') #removed new line character
           # print(line)
            temp_list=line.split() #default is any white  space split the string
           # print(temp_list)
            country = temp_list[0]
            capital = temp_list[1]
            #add extracted data to our dictionary where the country is our index value and the value is the capital
            the_world[country]=capital

#if the program doesn't know the capital, add it to our database
def write_to_file(country, capital):
    with open('capital_data.txt','a') as file:
        file.write('\n' + country + "   " + capital)

def fact_check(country,capital): ## rework function so that user is shown the correct capital if answered incorrectly
    with open('country-capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            print(row[0],row[1])
                if row[1] == capital: #the user is correct # if row[0] and row[1] wont work need nested loop
                    return True
                else:
                    return False #the user didn't guess the capital correctly


##########################################MAIN PROGRAM###########################################

read_from_file()

#start the infinite loop
while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country: ')
    query_country = query_country.lower().capitalize()
    if query_country in the_world: #if the input string is an index in the dictionary
        result = the_world[query_country]
        messagebox.showinfo('Answer',
                            'The capital city of '+ query_country + ' is ' + result)
    else:
        new_capital = simpledialog.askstring('Teach me',
                                             'I don\'t know the capital! What is the capital of ' + query_country + ' ?')
        new_capital = new_capital.lower().capitalize()
        if(fact_check(query_country,new_capital)): #fact check returns true  add it to dictionary and list
            the_world[query_country]=new_capital
            write_to_file(query_country,new_capital)
            messagebox.showinfo('Message',new_capital + ' is the capital of '+ query_country+ '! Adding it to database...')
        else:
            messagebox.showinfo('Message',new_capital + ' is not the captial of '+ query_country)

root.mainloop()