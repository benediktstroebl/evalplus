```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest
    Return the string with numbers sorted.
    """
    valid input: string containing numbers from zero to nine
    """
    return numbers.split(" ").
    map(strig_int, numbers. -1)
sort() 

def test_sort_numbers():
    """ Input is a space-delimited string of numbers from zero to nine """
    numbers = "zero one three five six seven eight nine"
    expected = "zero one three five six seven eight nine"
    print(sort_numbers(numbers))
    print(expected)

test_sort_numbers()
```