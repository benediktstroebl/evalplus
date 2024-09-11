### Maximum Element in List
#### Problem Statement:
Find the maximum element in a given list.

#### Solution:
```python
def max_element(l: list) -> int:
    """
    Return maximum element in the list.

    Args:
        l (list): The input list.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)
```
This script defines a function `max_element` that takes a list `l` as input and returns the maximum element in the list using Python's built-in `max` function.