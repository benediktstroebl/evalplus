```markdown
### Filter Integers from a List
#### Python Script

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): A list containing any type of python objects

    Returns:
        List[int]: A list containing only integers from the input list

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
print(filter_integers(['apple', 'banana', 'cherry']))  # Output: []
print(filter_integers([10, 20, 30, 'forty']))  # Output: [10, 20, 30]
```

### Explanation

This script uses a list comprehension to filter the input list and keep only the integers. The `isinstance(x, int)` function is used to check if each element `x` in the list is an instance of the `int` type.

The `filter_integers` function takes a list of any type of python objects and returns a new list containing only the integers from the original list.

The example usage at the end demonstrates how to use the `filter_integers` function with different input lists and shows the expected outputs.