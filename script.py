# Link til github: https://github.com/Mojens/python_mandatory_-assignment-_1

board_of_directors = {"Benny", "Hans", "Tine",
                      "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent",
             "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

# 1.1 who in the board of directors is not an employee?
not_employeed = board_of_directors - employees
print(not_employeed)

# 1.2 who in the board of directors is also an employee?
employeed = board_of_directors & employees
print(employeed)

# 1.3 how many of the management is also member of the board?
management_member_board = management & board_of_directors
total_management_member_board = len(management_member_board)
print(total_management_member_board)

# 1.4 All members of the managent also an employee?
management_employee = management & employees
print(management_employee)
# All members of the management is an employee

# 1.5 All members of the management also in the board?
management_board = management & board_of_directors
print(management_board)
# not all members of the management is in the board

# 1.6 Who is an employee, member of the management, and a member of the board?
employee_management_board = employees & management & board_of_directors
print(employee_management_board)

# 1.7 Who of the employee is neither a memeber or the board or management?
employee_not_board_management = employees - board_of_directors - management
print(employee_not_board_management)

# 2.1 Using a list comprehension create a list of tuples from the folowing datastructure
current_data_structure = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
tuplesList = list(current_data_structure.items())
print(tuplesList)

# 3.1 Create 2 sets
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}
print('Set 1: ', set1)
print('Set 2: ', set2)

# 3.2 Of the 2 sets create a: Union
unionSet = set1.union(set2)
print('Union: ', unionSet)

# 3.3 Of the 2 sets create a: symmetric difference
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference: ", symmetric_difference)

# 3.4 Of the 2 sets create a: difference
difference_set2_on_set1 = set2 - set1
print("Difference: ", difference_set2_on_set1)
difference_set1_on_set2 = set1 - set2
print("Difference: ", difference_set1_on_set2)

# 3.5 Of the 2 sets create a: disjoint
disJointSet = set1 & set2
print("Disjoint: ", disJointSet)

# 4.1 Create a dict suitable for decoding month names to numbers.
month_in_number = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
                   'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

# 4.2 & 4.3 Create a function which uses string operations to split the date into 3 items using the "-" character. & Translate the month, correct the year to include all of the digits.

def split_string_date(input_date):
    input = input_date.split('-')
    return input[0], month_in_number[input[1]], input[2]


print("Not formatted: 01-JAN-2019, Formatted: ",
      split_string_date('01-JAN-2019'))

# 4.2 & 4.3 (example with user input)
input_date = input('Enter date in format DD-MON-YYYY: ')
print(split_string_date(input_date))
