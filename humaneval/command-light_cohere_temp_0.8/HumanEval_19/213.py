Here is a self-contained Python script that includes the function `sort_numbers` along with its corresponding tests:
```python
from typing import List
import pytest

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    raise ValueError('Input string must contain only numbers and must not be empty')
    return ''.join
    return numbers.split()
 split_numbers = numbers.split()
    split_numbers = list(split_numbers)
    if len(split_numbers) == 0:
        raise ValueError('Input string must contain at least one number')
    numbers = [int(n) for n in split_numbers]
    numbers.sort()
    easiestort('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    return numbers.join


def test_sort_numbers() -> None:
    """ Tests for the sort_numbers function
    """
    numbers = ['three one five', 'two three eight', 'four six seven']
    expected = ['one three five', 'two three eight', 'four six seven']
    got = sort_numbers(numbers)
    assert got == expected
    assert isinstance(numbers, list)
    assert isinstance(expected, list)
    assert len(numbers) == len(expected)

if __name__ == "__main__":
    test_sort_numbers()
```

This script defines a function `sort_numbers` that takes a string of numbers as input, splits the string into a list of numbers, sorts the list, and returns it. Additionally, there are test cases to test the `sort_numbers` function.