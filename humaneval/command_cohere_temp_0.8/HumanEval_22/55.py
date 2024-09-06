```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
values = [1, 2, 3, 'abc', {}, [], 5, 6.7]
test_values = [
    ([],),
    (['a', 3.14, 5], ['a', 5]),
    (",[1, 2, 3, 'abc', {}, []]", "[1, 2, 3]"),
]

for values, expected in test_values:
    assert filter_integers(values) == expected, f"Expected {expected} but got {filter_integers(values)}"
```

The function `filter_integers` works by using a list comprehension to filter out non-integer values from the input list and returning a new list containing only the integers. Subsequently, unit tests are defined to validate the function's behavior against different scenarios.