### Max Element in a List
#### Problem Statement
Return the maximum element in a given list.

#### Solution
```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): Input list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, the `max_element` function uses the built-in `max` function in Python to find the maximum element in the input list. The `max` function takes an iterable as an argument and returns the maximum item in that iterable.