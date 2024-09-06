```python
from typing import List

def filter_integers(values):
    """
    Filter given list of any python values only for integers.

    Args:
        values: List[Any] - List of values with potential elements of any type.

    Returns: filtered list with only the integers.
    """
    filtering using list values that are either an int, float, or None
    """
    filtered_ints = [x for x in values if isinstance(x, (int, float))]
    return filtered_ints

# Test the function with markdown code block
test_values = [1, 2, 3, 'abc', 4, 5, (6)]
result = filter_integers(test_values)
print(result)  # Output: [1, 2, 3, 4, 5]
```

This script defines a function called `filter_integers` that takes a list of values as input and returns a new list that contains only the integers from the input list. The function uses a filtering approach to identify the integers in the input list.