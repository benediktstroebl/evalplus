```python
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
    values (List[Any]): A list of any python values

    Returns:
    List[int]: A list of integers
    """
    return [value for value in values if isinstance(value, int)]


# Test cases
print(filter_integers(['a', 3.14, 5]))  # Expected output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Expected output: [1, 2, 3]
```

In this script, we define a function `filter_integers` that uses a list comprehension to iterate over the input list `values`. For each value, it checks if the value is an instance of the `int` type using the `isinstance` function. If it is, the value is included in the output list; otherwise, it is skipped.

The test cases are included at the end of the script to verify the correctness of the function. You can run the script to see the expected output.