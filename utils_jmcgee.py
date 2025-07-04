"""
File: utils_jmcgee.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Jessyca McGee




"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variables (have a value True or False)
# TODO: Add another boolean variable before this one
has_professional_certification: bool = True
has_international_clients: bool = True

# declare integer variables
# TODO: Add another integer variable before this one
years_with_orgnization: int = 4
years_in_operation: int = 10

# declare a floating point variables
# TODO: Add another of floating point variable before this one
average_project_duration_hours: float = 6
average_client_satisfaction: float = 4.7

# declare lists of strings
# TODO: Add another list of strings before this one
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
addtional_skills_offered: list = ["Accounting", "Payroll", "Inventory Managment"]

# declare lists of numbers to illustrate statistics skills
# TODO: Add another numeric list before this one
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
project_duration_hours: list = [6, 5.5, 6.5, 5, 7]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: REPLACE the variable name, e.g. client_satisfaction_scores with your own numeric list variable name in all 4 lines below:
min_score: float = min(project_duration_hours)  
max_score: float = max(project_duration_hours)  
mean_score: float = statistics.mean(project_duration_hours)  
stdev_score: float = statistics.stdev(project_duration_hours)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the TEXT in the byline to describe your information
# TODO: Modify the VARIABLE NAMES in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Has Professional Certification: {has_professional_certification}
Years in Operation:         {years_in_operation}
Years with Orginzation: {years_with_orgnization}
Skills Offered:             {skills_offered}
Addtional Skills Offered: {addtional_skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Project Duration Hours: {project_duration_hours}
Minimum Project Hours Score: {min_score}
Maximum Project Hours Score: {max_score}
Mean Project Hours Score: {mean_score:.2f}
Standard Deviation of Project Hours Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_case.py")
    print(get_byline())
    print("END main() in utils_case.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()