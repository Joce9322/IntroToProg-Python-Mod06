# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   JMunoz,08/03/2024,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants

students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#Removed all of these and used them locally
    #student_first_name: str = ''  # Holds the first name of a student entered by the user.
    #student_last_name: str = ''  # Holds the last name of a student entered by the user.
    #course_name: str = ''  # Holds the name of a course entered by the user.
    #student_data: dict = {}  # one row of student data
    #csv_data: str = ''  # Holds combined string data separated by a comma.
    #json_data: str = ''  # Holds combined string data in a json format.
    #file = None  # Holds a reference to an opened file.

# Processing --------------------------------------- #
class FileProcessor:
    """
        A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created Class
    """
    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_data_from_file(file_name: str, student_data:list):
        """
            This function reads student registration data from a json file

            ChangeLog: (Who, When, What)
            JMunoz,8.3.2024,Created Function

            :param file_name: string for the file name
            :param student_data: list of dictionary rows containing student registration content
            :return student_data
        """
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data:list):
        """
            This function writes student registration data to a json file

            ChangeLog: (Who, When, What)
            JMunoz,8.3.2024,Created Function

            :param file_name: string for the file name
            :param student_data: list of dictionary rows containing student registration content
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
        A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param message: string displaying custom error messager
        :param Exception: exception to print
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param menu: string displaying the menu message
        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data:list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param student_data: list of dictionary rows containing student registration content
        :return: student_data: list of dictionary rows containing student registration content
        """
        #Input student data
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data:list):
        """ This function outputs the current students registered for courses

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param student_data: list of dictionary rows containing student registration content
        :return: None
        """
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        print()

#End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the following tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1": #Register a student for a course
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2": #Display registered students
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3": #Save data to file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4": #Exit program
        break #out of the while loop

print("Program Ended")
