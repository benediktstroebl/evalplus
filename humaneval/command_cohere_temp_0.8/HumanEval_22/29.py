```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

This function uses a list comprehension, which is a concise way to create a new list by applying a transformation to each item of the existing list. Here, the transformation checks if each item is an instance of the integer class, and if so, it includes it in the new list.

The type hint `List[Any]` is used to indicate that the function argument `values` can accept any type of value in the list. This allows you to pass various data types to the function without getting type hints errors. 

The function returns a list of integers after filtering the provided list. You can test this function by calling it with different lists of values, including various data types, and verifying that only the integers are filtered out. 

Here is an example of how to test this function with a different list input:
```python
filter_integers(['a', 3.14, 5])
# Output: [5]

filter_integers([1, 2, 3, 'abc', {}, []])
# Output: [1, 2, 3]
```

This way, you can ensure that the function works correctly for different inputs.