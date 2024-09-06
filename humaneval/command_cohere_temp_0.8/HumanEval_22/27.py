```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code directly addresses the problem statement by filtering `values` using a list comprehension based on the condition `isinstance(x, int)`.

This function can be tested by calling it with different inputs, such as:
```python
# Test with a list containing various values
test_list = ['a', 3.14, 5, 'foo', 7, True]
result = filter_integers(test_list)
print(result)  # Expected output: [5, 7]

# Test with a list containing only integers
test_list = [1, 2, 3, 'abc', {}, []]
result = filter_integers(test_list)
print(result)  # Expected output: [1, 2, 3]
```

The function should output `[5, 7]` for the first test case and `[1, 2, 3]` for the second test case.