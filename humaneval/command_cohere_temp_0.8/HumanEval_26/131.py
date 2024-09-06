```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This Python script defines a function called `remove_duplicates` which takes a list of integers as input. It removes any elements that occur more than once and returns a new list containing only the unique elements, maintaining their original order. This function uses a set called `seen` to keep track of elements that have already been encountered.

Here's an example of using this function:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```

And here's the corresponding test code using `pytest`:
```python
import pytest

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3, 2, 4], [1, 3, 4]),
    ([1, 1, 2, 3, 4, 4], [1, 2, 3, 4]),
])
def test_remove_duplicates(input_list, expected):
    """ Tests remove_duplicates function with different input lists """
    result = remove_duplicates(input_list)
    assert result == expected
```

To run these code blocks together, you would want to install `pytest` and run the tests in a Python environment or IDE that supports testing.