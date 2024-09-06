```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(' ')'.sort(map(int, split()))

# Tests:
assert sort_numbers('three one five') == 'one three five'
assert sort_numbers('six three') == 'six three'
assert sort_numbers('zero eight') == 'zero eight'
assert sort_numbers(' nine twelve thirty four ') == 'zero twelve thirtyfour'
``` 
The Python code defines a function `sort_numbers` that sorts a space-delimited string of numbers from 'zero' to 'nine'. The function splits the input into a list of numbers, sorts them, and then joins them back into a string.