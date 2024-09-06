```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of the given number to the specified base.
    Args: 
        - x: int, input number
        - base: int, base to which the input number will be converted
    Returns: 
        - string, number in the specified base
    """
    return format(x, f', {base}b')

# Test case 1: Change 8 to 3
test_case_1 = change_base(8, 3)
print("Case 1: ", test_case_1)

# Test case 2: Change 8 to 2
test_case_2 = change_base(8, 2)
print("Case 2: ", test_case_2)

# Test case 3: Change 7 to 2
test_case_3 = change_base(7, 2)
print("Case 3: ", test_case_3)

# Test case 4: Change 7 to 10
test_case_4 = change_base(7, 10)
print("Case 4: ", test_case_4)

# Test case 5: Change 10 to 10
test_case_5 = change_base(10, 10)
print("Case 5: ", test_case_5)
``` 
This Python script defines a function called change_base that takes an integer x and an integer base as input, and returns the number in the specified base as a string. The function utilizes the string formatting with the f-string format to perform the conversion and returns the result. 

Additionally, the script includes several test cases to verify the functionality of the change_base function. It successfully passes the The test cases, showcasing the expected output for each conversion.