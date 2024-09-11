Here's a Python script that implements the `filter_integers` function:
```markdown
### Filter Integers from a List of Any Values

#### Description

This script defines a function `filter_integers` that takes a list of any Python values and returns a new list containing only the integer values.

#### Code

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any python values only for integers

    Args:
        values (List[Any]): A list of any Python values

    Returns:
        List[int]: A new list containing only the integer values

    Examples:
        >>> filter_integers(['a', 3.14, 5])
        [5]
        >>> filter_integers([1, 2, 3, 'abc', {}, []])
        [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]

# Example usage:
if __name__ == "__main__":
    values1 = ['a', 3.14, 5]
    values2 = [1, 2, 3, 'abc', {}, []]

    print(filter_integers(values1))  # Output: [5]
    print(filter_integers(values2))  # Output: [1, 2, 3]
```

#### Explanation

The `filter_integers` function uses a list comprehension to iterate over the input list `values`. It uses the `isinstance` function to check if each value `x` is an instance of the `int` type. If it is, the value is included in the new list. The function returns this new list.

The example usage demonstrates how to call the `filter_integers` function with two different lists of values and print the resulting lists of integers.