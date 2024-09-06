```python
from typing import List
def sort_numbers(input_str: str) -> str:
    """ Sorts numbers in a string from lowest to highest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = list(map(int, input_str.sort())
   
   
    return ' '.join(str(sorted(numbers)))

# Test cases
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
assert sort_numbers('abc 123 456') == '456 123 abc'
```
The function takes a string input_str containing numbers in any order and returns a sorted version of that string. It uses the Python's map function to convert each number in the input string into its integer equivalent, and the sort() function to sort the numbers from lowest to highest. The sorted numbers are then converted back to strings and returned as a single string. The test_sort_numbers function tests the function with two input strings and checks if the output of the sort_numbers function matches the expected sorted strings.