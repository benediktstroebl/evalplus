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
values = [1, 2, 3, 'abc', {}, []]
test_values = [
    ([], []),
    (["a", 3.14, 5], [5]),
    (['a', 3.14, 5.0], [5.0]),
    (range(3), [0, 1, 2]),
    (values, [1, 2, 3]),
]
for args, expected in test_values:
    assert filter_integers(args) == expected, 'Failed to filter integers correctly.'
```

The function `filter_integers` checks if each value in the input list is an integer, and if so, adds it to the `integers` list, which it then returns. The test suite covers different scenarios to verify the function's correctness in filtering out integers from lists of different types of values.