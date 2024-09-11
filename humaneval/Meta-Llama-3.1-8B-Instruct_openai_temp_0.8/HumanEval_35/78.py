### Max Element in List
Max Element in List is a function that returns the maximum element in the given list.

#### Code
```python
def max_element(l: list):
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

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

#### Explanation
The `max_element` function takes a list as input and returns its maximum element. This is achieved using Python's built-in `max` function, which returns the largest item in an iterable. The function includes a docstring that describes its purpose, arguments, return value, and provides examples of its usage.