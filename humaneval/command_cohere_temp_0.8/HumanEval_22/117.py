```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
inputs = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]]
expected_outputs = [[5], [1, 2, 3]]

for input, output in zip(inputs, expected_outputs):
    assert filter_integers(input) == output
```

The `filter_integers` function iterates through the input list `values`. It processes each item `value` and checks if it can be converted to an integer using the `isinstance()` function. If it is, it is appended to the `integers` list. Finally, the function returns the `integers` list. The tests verify that the function produces the expected outputs for different inputs.