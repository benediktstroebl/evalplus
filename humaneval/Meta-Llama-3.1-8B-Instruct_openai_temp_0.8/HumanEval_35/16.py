```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)
```

To use this function, simply call it with a list of integers as an argument:

```python
numbers = [1, 2, 3, 4, 5]
print(max_element(numbers))  # Output: 5
```