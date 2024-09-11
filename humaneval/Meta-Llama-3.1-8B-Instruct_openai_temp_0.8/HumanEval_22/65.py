```markdown
### Filter Integers in a List of Python Values

#### Problem Description

Filter a list of any Python values and return a list of integers.

#### Solution

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any Python values.

    Returns:
        List[int]: A list of integers from the input list.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
```

#### Usage

To use this function, simply call it with a list of any Python values as an argument. The function will return a new list containing only the integers from the input list.

```python
# Example usage:
numbers_and_strings = [1, 2, 'hello', 3.14, 4, True]
integers = filter_integers(numbers_and_strings)
print(integers)  # Output: [1, 2, 4]
```

#### Explanation

The `filter_integers` function uses a list comprehension to create a new list containing only the integers from the input list. The `isinstance` function is used to check if each value in the input list is an instance of the `int` type. If it is, the value is included in the new list.