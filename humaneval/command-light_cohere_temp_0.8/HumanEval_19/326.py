```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    numbers = [int(num) for num in numbers.sort()
   
  a list(map(str.isdigit, numbers)))
    return ''.join(numbers)

def test_sort_numbers():
    return sort_numbers('three one five') == 'one three five'

print(test_sort_numbers())  # expected output: True
```

This Python code defines a function sort_numbers that sorts a list of numbers from a space-delimited string. The function uses a list comprehension and the built-in sort() function to convert the string of digits into a list of integers. The sorted list is then joined back into a string and returned. The test_sort_numbers function tests the function by calling it with an input string and comparing the returned string with the expected sorted string. The test passes the string that is sorted from smallest to largest.