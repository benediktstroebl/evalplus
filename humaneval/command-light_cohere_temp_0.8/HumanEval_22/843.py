```python
from typing import List

def filter_integers(values:
    """
    filtered = [x for x in values if isinstance(x, int)]
    return filtered

# Test cases
test_cases = [
    [['a', 3.14, 5'], [1, 2, 3, 'abc', {}, []]
]

for test in test_cases:
    actual = filter_integers(test)
    expected = [1, 2, 3]  # Corresponding integers in the expected output
    assert actual == expected, f"test case {test} failed: {actual} != {expected}"
```
The code defines a function `filter_integers` that takes a list of values and returns a new list containing only integers from the input. The function uses a filtering approach to achieve this. The code also provides a test cases to verify the correctness of the `filter_integers` function.