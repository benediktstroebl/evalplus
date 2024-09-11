### Increment List Elements
#### Solution

```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list.

    Returns:
        list: The incremented list.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```

#### Explanation
This script uses a list comprehension to create a new list where each element is the input list's element incremented by 1. The `for x in l` part iterates over each element in the list, and `x + 1` calculates the incremented value. The resulting incremented values are collected into a new list, which is then returned.

You can use this script as is, or incorporate it into your own project as a function.