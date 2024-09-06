```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are sort order from 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    # Remove non-numeric characters and convert string to integer array
    numbers = numbers.split()
    value_ numbers = [int(n) for n in numbers]
    # Sort numbers from smallest to largest
    sorted_numbers = sorted(value)
    # Join the sorted numbers into a string
    sorted_string = ' '.join([str(num) for num in sorted_numbers])
    return sorted_string

# Unit tests
test_sort_numbers = []
test_sort_numbers.append([str("three one five").split())
test_sort_numbers.append(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
# Validate the function's response
assertEqual(sort_numbers(test_sort_numbers[0]), 'one three five')
assertEqual(sort_numbers(test_sort_numbers[1]), 'two three four five six seven eight nine')
``` 
This script defines a function `sort_numbers` that sorts a given string of numbers. The function takes a string of numbers and removes non-numeric characters. It then converts the string to an array of integers and finally sorts the array. The unit tests section contains a series of test cases, and the `assertEqual` function checks if the function's response matches the expected result.