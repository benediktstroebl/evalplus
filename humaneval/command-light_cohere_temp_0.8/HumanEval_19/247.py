```python
import typing
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Numbers are case-sensitive, so '3 One 5' would not be valid.
    Return the if a string with numbers sorted from smallest to largest.
    """
    string = numbers.split(' ')
    all at least
       
    numbers = [int(num.strip()) for num in numbers]
    numbers.sort()  #all positive integers)
    # remove non-integer numbers
    numbers = [num for num in numbers if isinstance(num, int)]
    numbers = ' '.join(str(num) for num in numbers)
    return numbers

# test cases
test_str = 'three one five'
sorted_test = sort_numbers(test_str)
print(sorted_test)  # expected output: one three five'

test_str = 'zero one two three four five six seven eight nine'
sorted_test = sort_numbers(test_str)
print(sorted_test)  # expected output: zero one two three four five six seven eight nine'

test_str = 'abc123XYZ456 abc'
sorted_test = sort_numbers(test_str)
print(sorted_test)  # expected output: abc123XYZ456  (due to case sensitivity)

test_str = '1 two three four five six seven eight nine'
sorted_test = sort_numbers(test_str)
print(sorted_test)  # expected output: one two three four five six seven eight nine'
```