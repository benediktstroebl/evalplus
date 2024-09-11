```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
    l (list): A list of elements

    Returns:
    The maximum element in the list

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(l)  # Return the maximum element in the list

# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
This script defines a function `max_element` that takes a list as input and returns its maximum element. If the list is empty, it raises a ValueError. The function uses the built-in `max` function to find the maximum element.