### Maximum Element in a List
#### Problem Statement

Write a Python function `max_element` that takes a list of numbers as input and returns the maximum element.

#### Solution
```python
def max_element(lst: list) -> int:
    """Return the maximum element in the list.
    
    Args:
        lst (list): A list of numbers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
This function uses the built-in `max` function in Python to find the maximum element in the list. It checks if the list is empty before attempting to find the maximum element, and raises a `ValueError` if the list is empty.