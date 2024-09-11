```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing any type of python values

    Returns:
        List[int]: A list containing only the integers from the input list
    """
    return [value for value in values if isinstance(value, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
```

In this script, we define a function `filter_integers` which uses a list comprehension to filter the input list `values`. The `isinstance(value, int)` condition ensures that only integers are included in the output list.

The test cases at the end of the script demonstrate the function's behavior. The `filter_integers` function is called with different input lists, and the expected output is printed to the console.