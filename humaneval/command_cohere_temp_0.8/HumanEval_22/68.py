```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result

# Tests
inputs = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

expected_results = [
    [5],
    [1, 2, 3],
]

for input, expected in zip(inputs, expected_results):
    result = filter_integers(input)
    assert result == expected
```

The function `filter_integers` takes a list of values of any type and returns a list of integers. It iterates through each value in the input list, and if the value is an integer, it is added to the result list. The function returns the result list populated only with integers. 

The tests verify that the function correctly identifies and returns integers from the input lists, producing the expected results.

Let me know if this solution works for you and if you would like to further discuss any aspects of the code or other solutions you might consider.