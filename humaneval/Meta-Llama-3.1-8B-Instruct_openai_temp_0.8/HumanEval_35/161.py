### Max Element in List
#### Problem Description

Return the maximum element in a given list.

#### Solution

```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
    lst (list): A list of elements.

    Returns:
    The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(lst)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we utilize Python's built-in `max()` function to find the maximum element in the list. This approach is concise and efficient.