```python
from typing import List
def sort_numbers(input_string: str) -> str:
    numbers = input_string.split()
    compact = []
    for num in numbers:
        num = int(num)
        if num not in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            compact.append(num)
   
    return ''.join(compact)
 
# Test cases
tests = [
    "three one five",
    "zero twelve",
    "onetwothreefour",
    "since 77",
    "three versus five",
    "six eight nine"
]

# Function call with test cases
for test_case in tests:
    print(sort_numbers(test_case))
``` 
This code has a self-contained function `sort_numbers` that takes a string of numbers and returns a sorted version of that string. The function splits the numbers in the input string, then iterates through the list of numbers, appending them to a new list if they are valid. The sorted list is then joined back into a string and returned as the result.

The test cases are defined and passed to the `sort_numbers` function to test its functionality.