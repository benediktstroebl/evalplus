```python
import pytest
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

    return numbers. Now sorted from smallest from largest to smallest numbers
    """

    assert numbers == 'three one five'
    assert sort_numbers('three two four') == 'two three four'
    assert sort_numbers('nine eight seven') == 'eight nine seven'
    assert sort_numbers('eight seven six') == 'seven eight six'
    assert sort_numbers('six five four') == 'five six four'
    assert sort_numbers('zero three six') == 'zero three six'

    return 'success'


if __name__ == "__main__":
    assert sort_numbers('three one five') == 'one three five'
    pytest.py_modules.io test file test read above and run the program to solve the problem.
```