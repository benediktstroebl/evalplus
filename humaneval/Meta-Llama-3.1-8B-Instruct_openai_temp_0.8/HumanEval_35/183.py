### Max Element in List
#### Problem: Find the maximum element in a given list

```python
def max_element(l: list) -> int:
    """
    Return maximum element in the list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script uses the built-in `max` function in Python to find the maximum element in the list, making it concise and efficient. The `max` function takes an iterable as an argument and returns the largest item in that iterable.