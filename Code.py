################################################################################################
# Program Name: Student Admissions System
# Description: This program facilitates the admission process for Humber College. It prompts the user
#              for a password, validates it, and then gathers information about the number of students,
#              their names, and grades. Based on the grades, it calculates GPAs and assigns schools.
#              Finally, it generates reports showing the distribution of students among different schools
#              and the percentage of students accepted in each school.
# Author: Vidhya Shanker, Himalay, Haris
# Date: 17/04/2024
#
# Usage:
# - Run the script.
# - Follow the prompts to enter the required information.
# - Reports will be displayed at the end of the process.
#
# Note: This program assumes a specific password policy and grading system. It may need adjustments
#       to fit different requirements.
#################################################################################################

import tkinter as tk  # Importing tkinter module as tk for easier reference
from tkinter import messagebox, simpledialog  # Importing messagebox and simpledialog from tkinter

import re  # Importing the regular expression module for pattern matching

def welcome_message():  # Function to display a welcome message
    messagebox.showinfo("Welcome", "Welcome to Humber College")  # Showing a welcome message using a messagebox

def check_password():  # Function to prompt the user for password input and validate it
    attempts = 3  # Initializing number of password attempts allowed
    while attempts > 0:  # Looping until no attempts left
        password = simple_input("Enter your password: ")  # Prompting user for password input
        if len(password) < 10:  # Checking if password length is less than 10 characters
            messagebox.showerror("Error", "Password should be at least 10 characters long.")  # Showing error message
        elif not any(char.isupper() for char in password):  # Checking if password contains at least one uppercase letter
            messagebox.showerror("Error", "Password should contain at least one upper case letter.")  # Showing error message
        elif not 2 <= len(re.findall(r'\d', password)) <= 3:  # Checking if password contains 2 to 3 numbers
            messagebox.showerror("Error", "Password should contain at least two and at most three numbers.")  # Showing error message
        elif not any(char in '!@#$%^&*()_+-=[]{};:\'",.<>?/' for char in password):  # Checking if password contains a special character
            messagebox.showerror("Error", "Password should contain one special character.")  # Showing error message
        else:
            return password  # Returning password if all conditions are met
        attempts -= 1  # Decrementing attempts
        if attempts > 0:  # Checking if attempts are still remaining
            messagebox.showinfo("Attempts", f"Remaining attempts: {attempts}")  # Showing remaining attempts
        else:
            messagebox.showerror("Error", "Maximum attempts reached. Exiting program.")  # Showing maximum attempts reached
            exit()  # Exiting program if maximum attempts reached

def get_number_of_students():  # Function to prompt the user for number of students input and validate it
    attempts = 3  # Initializing number of attempts allowed
    while attempts > 0:  # Looping until no attempts left
        try:
            number_of_students = int(simple_input("Enter the number of students (1-50): "))  # Prompting user for number of students input
            if 1 <= number_of_students <= 50:  # Checking if input is within valid range
                return number_of_students  # Returning number of students if valid
            else:
                messagebox.showerror("Error", "Please enter a number between 1 and 50.")  # Showing error message
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")  # Showing error message
        attempts -= 1  # Decrementing attempts
    messagebox.showerror("Error", "Maximum attempts reached. Exiting program.")  # Showing maximum attempts reached
    exit()  # Exiting program if maximum attempts reached

def get_student_names(number_of_students):  # Function to prompt the user for student names input and validate them
    student_names = []  # Initializing list to store student names
    for i in range(number_of_students):  # Iterating over the range of number of students
        while True:  # Looping until valid input is received
            student_name = simple_input(f"Enter the name of student {i + 1}: ").strip()  # Prompting user for student name input
            if not student_name.isalpha():  # Checking if name contains only alphabetic characters
                messagebox.showerror("Error", "Name must contain only alphabetic characters. Please try again.")  # Showing error message
            elif not student_name.istitle():  # Checking if name is in title case
                messagebox.showerror("Error", "Name must be in title case (e.g., John). Please try again.")  # Showing error message
            else:
                break  # Breaking out of loop if input is valid
        student_names.append(student_name)  # Adding valid student name to the list
    return student_names  # Returning list of student names

def get_student_grades(student_names):  # Function to prompt the user for student grades input and validate them
    student_grades = []  # Initializing list to store student grades
    courses = ['Math', 'Science', 'Language', 'Drama', 'Music', 'Biology']  # List of courses
    for student_name in student_names:  # Iterating over student names
        grades = []  # Initializing list to store grades for current student
        for course in courses:  # Iterating over courses
            while True:  # Looping until valid input is received
                try:
                    grade = float(simple_input(f"Enter the grade of {course} for {student_name}: "))  # Prompting user for grade input
                    if 0.0 <= grade <= 100.0:  # Checking if grade is within valid range
                        if grade < 40:  # Checking if grade is below passing threshold
                            messagebox.showerror("Error", "Grade must be 40 or above. Please try again.")  # Showing error message
                        else:
                            grades.append(grade)  # Adding valid grade to the list
                            break  # Breaking out of loop if input is valid
                    else:
                        messagebox.showerror("Error", "Grade must be between 0.0 and 100.0. Please try again.")  # Showing error message
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid numeric grade.")  # Showing error message
        student_grades.append(grades)  # Adding list of grades for current student to the main list
    return student_grades  # Returning list of student grades

def calculate_gpa(student_grades, credit_hours):  # Function to calculate GPA for each student
    gpa_list = []  # Initializing list to store GPAs
    for grades in student_grades:  # Iterating over list of student grades
        total_grade_points = sum(grade * credit_hour for grade, credit_hour in zip(grades, credit_hours))  # Calculating total grade points
        total_credit_hours = sum(credit_hours)  # Calculating total credit hours
        gpa = total_grade_points / total_credit_hours  # Calculating GPA
        gpa_list.append(gpa)  # Adding GPA to the list
    return gpa_list  # Returning list of GPAs

def assign_schools(gpa_list):  # Function to assign schools based on GPAs
    school_distribution = {'Engineering': 0, 'Business': 0, 'Law': 0, 'Not accepted': 0}  # Dictionary to store school distribution
    for gpa in gpa_list:  # Iterating over list of GPAs
        if 90 <= gpa <= 100:  # Checking GPA range
            school_distribution['Engineering'] += 1  # Incrementing count for Engineering
        elif 80 <= gpa < 90:  # Checking GPA range
            school_distribution['Business'] += 1  # Incrementing count for Business
        elif 70 <= gpa < 80:  # Checking GPA range
            school_distribution['Law'] += 1  # Incrementing count for Law
        else:
            school_distribution['Not accepted'] += 1  # Incrementing count for Not accepted
    return school_distribution  # Returning school distribution

def print_reports(student_names, gpa_list, school_distribution):  # Function to print reports
    report_text = ""  # Initializing report text
    report_text += "\nReport 1: Student Name, School Name\n"  # Adding report heading
    for student_name, gpa in zip(student_names, gpa_list):  # Iterating over student names and GPAs
        if 90 <= gpa <= 100:  # Checking GPA range
            school = 'Engineering'  # Assigning school
        elif 80 <= gpa < 90:  # Checking GPA range
            school = 'Business'  # Assigning school
        elif 70 <= gpa < 80:  # Checking GPA range
            school = 'Law'  # Assigning school
        else:
            school = 'Not accepted'  # Assigning school
        report_text += f"{student_name}, {school}\n"  # Adding student name and school to report text

    report_text += "\nReport 2: Number of accepted students in Humber college showing students distribution per each school.\n"  # Adding report heading
    total_accepted = sum(school_distribution.values()) - school_distribution['Not accepted']  # Calculating total accepted students
    if total_accepted == 0:  # Checking if no students accepted
        report_text += "No students accepted in any school.\n"  # Adding message
    else:
        for school, count in school_distribution.items():  # Iterating over school distribution
            if school != 'Not accepted':  # Excluding 'Not accepted' category
                report_text += f"Number of students in {school}: {count}\n"  # Adding count for each school
        report_text += f"Number of students not accepted: {school_distribution['Not accepted']}\n"  # Adding count for not accepted students

    report_text += "\nReport 3: Number of students that not accepted.\n"  # Adding report heading
    report_text += f"Number of students not accepted: {school_distribution['Not accepted']}\n"  # Adding count for not accepted students

    report_text += "\nReport 4: Percentage of students accepted in each school.\n"  # Adding report heading
    if total_accepted != 0:  # Checking if any students accepted
        for school, count in school_distribution.items():  # Iterating over school distribution
            if school != 'Not accepted':  # Excluding 'Not accepted' category
                percentage_accepted = (count / total_accepted) * 100  # Calculating percentage of students accepted
                report_text += f"Percentage of students accepted in {school}: {percentage_accepted:.2f}%\n"  # Adding percentage to report text

    messagebox.showinfo("Reports", report_text)  # Displaying reports using a messagebox

def simple_input(prompt):  # Function to display a simple input dialog and get user input
    root = tk.Tk()  # Creating tkinter root window
    root.withdraw()  # Hiding the root window
    return simpledialog.askstring("Input", prompt)  # Displaying simple input dialog and returning user input

def main():  # Main function to execute the program
    welcome_message()  # Displaying welcome message
    password = check_password()  # Getting and validating password
    number_of_students = get_number_of_students()  # Getting and validating number of students
    student_names = get_student_names(number_of_students)  # Getting and validating student names
    student_grades = get_student_grades(student_names)  # Getting and validating student grades
    credit_hours = [4, 5, 4, 3, 2, 4]  # List of credit hours for courses
    gpa_list = calculate_gpa(student_grades, credit_hours)  # Calculating GPAs
    school_distribution = assign_schools(gpa_list)  # Assigning schools based on GPAs
    print_reports(student_names, gpa_list, school_distribution)  # Printing reports

if __name__ == "__main__":  # Checking if the script is executed directly
    main()  # Calling the main function to start the program
