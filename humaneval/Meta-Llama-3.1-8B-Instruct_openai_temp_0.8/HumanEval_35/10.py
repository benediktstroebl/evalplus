### Max Element in a List
#### Problem: Find the maximum element in a list
#### Solution: Python Function
```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
    l (list): The list to find the maximum element in.

    Returns:
    int: The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
This script defines a function `max_element` that takes a list `l` as input and returns its maximum element using Python's built-in `max` function. The function includes a docstring with examples of usage for clarity and testing.