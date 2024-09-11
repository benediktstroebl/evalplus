```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")

    # Use the built-in max function to find the maximum element
    return max(l)
```

You can use this function like this:
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```