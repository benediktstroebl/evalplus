```python
def max_element(l: list):
    """Return maximum element in the list.
    Args:
        l (list): A list of elements.
    Returns:
        int or float: The maximum element in the list.
    Raises:
        ValueError: If the list is empty.
    """
    if not l:
        raise ValueError("Cannot find max of an empty list")
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
This Python script defines a function `max_element` that takes a list as input and returns the maximum element in the list. If the list is empty, it raises a `ValueError`. The function uses the built-in `max` function, which returns the largest item in an iterable or the largest of two or more arguments.