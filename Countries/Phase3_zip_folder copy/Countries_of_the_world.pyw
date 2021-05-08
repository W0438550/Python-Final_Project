import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox
from PyQt5.QtGui import QPixmap


#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_Countries_of_the_world
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_Countries_of_the_world.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    #Declare a global list
    CountriesList = []

    unsaved_changes = False

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
         # slot for when an item is selected in the list
        self.listWidgetPopulation.currentRowChanged.connect(self.RowChange)
        # slot for when the load countires command in the menu is clicked
        self.actionLoad_Countries.triggered.connect(self.LoadMenu_Triggered)
        #slot for when the  mile radio button is clicked
        self.radioButtonMile.clicked.connect(self.SquareMileRadioButton)
        #slot for when the km radio button is clicked
        self.radioButtonKM.clicked.connect(self.SquareKMRadioButton)
        #slot for when the update push button is clicked
        self.pushButtonPopulation.clicked.connect(self.UpdatePopulation)
        #slot for when the combox options are clicked
        self.comboBoxArea.currentIndexChanged.connect(self.ComboBox)
        #slot for when exiting the program when the exit button has been clicked
        self.actionExit.triggered.connect(self.exit_program)
        #slot for setting the save to file action to false 
        self.actionSave_To_File.setEnabled(False)
        #slot for when the save to file button has been clicked
        self.actionSave_To_File.triggered.connect(self.saveChanges)

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)
    # Create a function that contains other slot functions. This function will call the other functions and run it.
    # This function will call the functions containing the file containing the list of the countries, 
    # call the function that adds the country names to the list widget and call the function that displays the combo box value(Sq. Miles and Sq. KMs)
    # when the load button is clicked
    def LoadMenu_Triggered(self,Index):
        self.LoadDataFromFile()
        # self.LoadFromMemtoListWidget()
        self.LoadCountryNames()
        self.TotalArea(Index)

    # This function was created once the user selects a country from the list widget. It will retreive the index positions of the country name, area and population.
    def RowChange(self,Index):
        countryName = self.CountriesList[Index][0]
        countryPopulation = int(self.CountriesList[Index][1])
        countryArea = float(self.CountriesList[Index][2])

        #This part of the function displays the values of the country name, population, area, country flag, population density
        # percentage of world population, the initial value for the combo box(Sq. Miles) for each country.
        #Set the text of the two lineedits to the name/age values
        self.labelName.setText(countryName)
        self.lineEditPopulation.setText(f"{countryPopulation:,}")
        self.labelArea_2.setText("{0:,.1f}".format(countryArea))
        self.FlagName(countryName)
        self.PopulationDensity(Index)
        self.PercentagePopulation(countryPopulation)
        self.radioButtonMile.setChecked(True)
        self.comboBoxArea.setCurrentText("Sq. Miles")

    #This function retrieves the country flag. A function called QPixmap has to be imported to allow the flags to be displayed.
    #The country names with a space are replaced by an underscore so that they can be displayed. p.s they were not being displayed before.     
    def FlagName(self,countryName):
        cntName = countryName.replace(" ","_")
        countryFlag = QPixmap(f"Flags\\{cntName}.png")

        self.labelFlag.setPixmap(countryFlag)

    # This function calculates the population density by dividing the index values of 1(contains population) and the index values of 2(contains area)
    # It then displays it to 2 decimal places next to the population density label on the GUI.
    def PopulationDensity(self,Index):
        countryPopulation = int(self.CountriesList[Index][1])
        countryArea = float(self.CountriesList[Index][2])
        population_Density = countryPopulation / countryArea

        self.labelDensity_2.setText("{0:.2f}".format(population_Density))

    # This function calculates the percentage of the world population. A for loop is runned that goes through all values of the population
    # and adds them together and store them in a variable. The percentage is then calculated using that value and the value of th selected country.
    # displays the value to 4 decimal places.
    def PercentagePopulation(self,countryPopulation):
        sumPopulation = 0
        rowValue = 0.0

        for rowValue in self.CountriesList:
            sumPopulation = float(sumPopulation + float(rowValue[1]))
            
        worldPopulation = float((100/sumPopulation) * (countryPopulation))
        
        self.labelPercentage_2.setText(f"{worldPopulation:.4f}%")

    # This function was created for the square mile radio button. It takes in the values of the current Index that is selected,
    # the country population(index 1) and the country area(index 2). It then calculates the population density by dividing the country population by the country area
    # Displays the population density to 2 decimal places.
    def SquareMileRadioButton(self):
        rIndex = int(self.listWidgetPopulation.currentRow())
        countryPopulation = float(self.CountriesList[rIndex][1])
        countryArea = float(self.CountriesList[rIndex][2])
        
        population_Density_SquareMile = countryPopulation / countryArea
        
        self.labelDensity_2.setText(f"{population_Density_SquareMile:.2f}")

    # This function was created for the square KM radio button. It takes in the values of the current Index that is selected,
    # the country population(index 1) and the country area(index 2). It then calculates the population density by dividing the country population by the country area
    # Displays the population density to 2 decimal places.
    def SquareKMRadioButton(self):
        rIndex = int(self.listWidgetPopulation.currentRow())
        countryPopulation = float(self.CountriesList[rIndex][1])
        countryArea = float(self.CountriesList[rIndex][2])

        population_Density_SquareKM = (countryPopulation / countryArea) * (2.59)

        self.labelDensity_2.setText(f"{population_Density_SquareKM:.2f}")

    # This function was created for the update population push button and display label. It takes the current value of the Index that is selected
    # displays the population before update, then replaces each comma with an empty string; stores it in a new variable
    # assigns a new variable to the selected index by the user, does a data type check on the value entered by the user, display a combo box if data is valid and invalid depending on whether the value is numeric or not.
    # the new value is displayed, stored in the current list and is saved in the txt file(countries.txt)
    # the load countries button is also disabled and th save country button is enabled
    def UpdatePopulation(self,Index):
        
        rIndex = int(self.listWidgetPopulation.currentRow())
        # countryPopulation = float(self.CountriesList[rIndex][1])
        populationOriginal = self.lineEditPopulation.text()
        populationUpdate = populationOriginal.replace(",", "")
        populationUpdate1 = self.CountriesList[rIndex][1]

        try:
            populationUpdate1 = int(populationUpdate)
           
        except ValueError:
             QMessageBox.information(self, 'Not Updated', 'Data is invalid so not updated in memory', QMessageBox.Ok)
             self.unsaved_changes = False
        
        self.CountriesList[rIndex][1] = populationUpdate1
        self.lineEditPopulation.setText(f"{populationUpdate1:,}")
        QMessageBox.information(self,'Updated','Data has been updated in memory, but hasn''t been updated in the file yet', QMessageBox.Ok)
        self.unsaved_changes = True
        self.actionSave_To_File.setEnabled(True)
        self.actionLoad_Countries.setEnabled(False)

    # This function was created for the combo box. It takes in the values of the current Index that is selected,
    # the country area(index 2). It then calculates the area in KM. Uses and if statement to compare the selected choice of the user
    # between Sq.Miles and Sq. KMs and display each text accordingly.
    def ComboBox(self,Index):
        rIndex = int(self.listWidgetPopulation.currentRow())
        countryAreaMiles = float(self.CountriesList[rIndex][2])
        countryAreaKM = (countryAreaMiles * 2.59)
    
        userIndex = self.comboBoxArea.itemText(Index)

        if(userIndex == "Sq. Miles"):
            self.labelArea_2.setText(f"{countryAreaMiles:,.1f}")
        elif(userIndex == "Sq. KMs"):
            self.labelArea_2.setText(f"{countryAreaKM:,.1f}")

    # This function was created to display a pop-up box when the user is closing the GUI. If the user saves the changes made,
    # the save is made to the file. 
    def closeEvent(self, event):

        if self.unsaved_changes == True:

            msg = "Save changes to file before closing?"
            reply = QMessageBox.question(self, 'Save?',
                     msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.save_changes_to_file()
                event.accept()

    # This function was created to access the country file and write to it to allow changes to the file. Works with the update popualtion function.
    def saveChanges(self):
        accessMode = "w"
        with open("countries.txt",accessMode) as countryFile:
            for country in self.CountriesList:
                countryFile.write(",".join(country) + "\n")

    # This function was created to allow the user to use the exit button to close the GUI window.   
    def exit_program(self):
        QApplication.closeAllWindows()

#Example Slot Function
#   def SaveButton_Clicked(self):
#       Make a call to the Save() helper function here

    #ADD HELPER FUNCTIONS HERE
    # These are the functions the slot functions will call, to 
    # contain the custom code that you'll write to make your progam work.
    # Indent to this level (ie. inside the class, at same level as def __init__)
    
    # This function was created to add the various countries to the list widget.
    def LoadCountryNames(self):
        # country = self.CountriesList[index][0]
        # self.listWidgetPopulation.setText(country)
        for row in self.CountriesList:
            country = row[0]
            self.listWidgetPopulation.addItem(country)

    # This function was created to load the country file as a csv file so that it can be edited for further purposes.
    # The values of the file is added to a list. The file needs to be closed. 
    def LoadDataFromFile(self):
        import csv
        
        fileName = "countries.txt"
        accessMode = "r"

        myFile = open(fileName,accessMode)
        fileContents = csv.reader(myFile)

        self.CountriesList = [] #Clear the list before loading it from the file.

        for row in fileContents:
            self.CountriesList.append(row)
            # print(row[0])

        myFile.close()

    # This function was created to add the Sq. Miles and Sq. KMs values to the combo box as text. The text is displayed based on the selection of the user but is by default set to Sq. Miles.    
    def TotalArea(self,Index):
        self.comboBoxArea.addItem("Sq. Miles")
        self.comboBoxArea.addItem("Sq. KMs")

#Example Helper Function
#    def Save(self):
#       Implement the save functionality here

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY