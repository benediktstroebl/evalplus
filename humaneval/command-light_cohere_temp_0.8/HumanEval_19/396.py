```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Returns the string with numbers sorted from smallest to largest.
    """
   
   
    input
    return sorted_numbers(input_str)

def sorted_numbers(input_str):
    # remove spaces and convert to list of numbers
    numbers = input_str.split()
   
    number_list = list(map(int, numbers))
    # sort the list of numbers
    return sorted(number_list)

# run test cases
input_cases = ["three one five", "five six three", "six seven eight nine"]

for input_case in input_cases:
    expected = ["one", "three", "five"]
    got = sorted_numbers(input_case)
    print(f"Expected: {expected}, Got: {got}")
    print(f"Error: {input_case} not sorted correctly.")
``` 
This script contains a self-contained function that takes a string of numbers and returns a sorted version of the numbers. The function sorts the numbers from smallest to largest by converting them to a list and then using the sorted function to sort the list.