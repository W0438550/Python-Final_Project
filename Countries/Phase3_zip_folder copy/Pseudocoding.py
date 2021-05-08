#Final Project pseudocoding 

#Phase1 - Designs the GUI interface on QT Designer

#Use a widget list for the country lists
#Use a label for the country names
#Use a label to display the Population
#Use a line edit box to allow the output of the Population
#Use a push button box to allow update of the Population
#Use a label for the total area
#use a combo box to display the value of the area in square miles and kilometres
#use a label to display the Population Density text
#Use radio buttons one for Square Mile and on for Square KM to allow change to display as per user choice.
#use a label to diplay the Percentage of the World Population text
#use text label to display the output of the percentage population

#Phase2 - Write the codes to allow major functionality of the main window

#Created a slot function for the displaying of the list countries in the widget list.
#Opened the txt as a csv file to read the data in it.
#the country name was read at row index 1, the country population was read at row index 2 and the country area was read at row index 3.

#Create a slot function for the flag image
#the flag images was read from the file(p.s use relative path of the file)

#Create a slot function function for the population density 
#The population density was calculated using the country population(Index[2] in file) and country area(Index[3] in file) using division
#The value was set to 2 decimal places.

#Create a slot function for the world percentage pouplation
#Run a for loop to find the sum of the all the countries' population
#divide the sum of the population with the pouplation of the selected country in the list.

#Phase 3 - Write the code to allow functionality for both radio buttons, update push button, pop-up save of all data changes to the original text.

#Create a slot function for square mile radio button 
#use a new index  to import the value of the countries
#use the index value of the country's population and the index value of the country's area
#divide the country popualtion with the country area 

#Create a slot function for KM radio button 
#use a new index  to import the value of the countries
#use the index value of the country's population and the index value of the country's area
#divide the country popualtion with the country area multiplied by the converion rate(2.59)

#Create a function for the update population
#import the new index(rIndex) and the country population
#replace the commas with an empty string for the population
#run a datatype check and check for the index 1 for the population values.


