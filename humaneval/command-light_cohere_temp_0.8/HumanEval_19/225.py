```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string is 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.
    # Use an InPylist to convert space-separated numbers into a list
    numbers_list = [int(num) for num in numbers.
    # Sort the array of numbers from smallest to largest
    numbers_array = sorted(numbers_list)
    # Join the sorted list back into a string
    return ' '.join(str(num) for num in numbers_array)

# Test cases
test_cases = [
    "three one five",
    "zero one three",
    "two three four",
    "five six seven eight nine"
]

# Function Call and Results
for test_case in test_cases:
    print(sort_numbers(test_case))
```
This script defines a function `sort_numbers` that takes a space-separated string of numbers and returns the sorted version of that string. It then defines a array of test cases with various numbers, and for each test case, it prints the result of the function call with the test case as the output.