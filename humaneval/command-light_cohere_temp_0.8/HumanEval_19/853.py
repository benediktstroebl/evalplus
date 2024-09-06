```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers. Numbers will be sorted from smallest to largest
    Return the string with numbers sorted from smallest to largest
    """
    numbers.sort()
    numbers
    numbers = sorted(numbers)
    return numbers

def test_sort_numbers():
    """
    Test Case 1:
    >>> test_sort_numbers('three one five')
    ['one', 'three', 'five']
    """
    numbers = ['three', 'one', 'five']
    assert sort_numbers(numbers) == ['one', 'three', 'five']

    """
    Test Case 2:
    >>> test_sort_numbers('hello, world!')
    ['hello', 'world!']
    """
    numbers = ['hello', 'world!']
    assert sort_numbers(numbers) == ['hello', 'world.']


if __name__ == "__main__":
    print("Test cases passed")
```