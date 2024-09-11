Here's a Python script that implements the `filter_integers` function as specified in the docstring:

```markdown
### Filter Integers from a List of Any Python Values
#### Python Script
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list containing values of any python type.

    Returns:
        List[int]: A list of integers found in the input.

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Testing the function with example inputs
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))
    print(filter_integers([1, 2, 3, 'abc', {}, []]))
```
This script uses a list comprehension to create a new list containing only the integers from the input `values` list. The `isinstance(value, int)` condition checks if a value is an integer before including it in the output list.