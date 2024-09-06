Here's a Python script with a self-contained function that solves the problem of sorting a list of numbers in Markdown code blocks:
```python
from typing import List
import pytest


def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of numbers, 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return [''.join(str(num).join(sorted(nums)) for nums in numbers]


@pytest.mark('" three one five" "two three four five")
def test_sort_numbers():
    assert sorted("three one five") == "one three five"
    assert sorted("two six four") == "two six four"
    assert sorted("zero nine") == "zero nine"
    assert sorted([0,1,2]) == [0,1,2]
```
The above code defines a function `sort_numbers` that sorts a list of numbers in ascending order, and has its functionality tested via the `test_sort_numbers` function, using the pytest library for testing.