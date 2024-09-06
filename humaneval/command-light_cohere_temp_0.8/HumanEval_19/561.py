Here's a Python script that defines a function `sort_numbers` to sort an input string of numbers in ascending order:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(' ', ')[:-1].
            .sort()
            .join()
            .join()
            .replace(' ', '')

def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
```
The `sort_numbers` function splits the input string by spaces, sorts the resulting list from smallest to largest, and then joins the sorted list back into a string.