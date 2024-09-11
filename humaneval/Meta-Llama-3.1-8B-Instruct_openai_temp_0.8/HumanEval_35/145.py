```python
# Define a function to find the maximum element in a list
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
    l (list): A list of elements.

    Returns:
    element: The maximum element in the list.

    Raises:
    ValueError: If the list is empty.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:  # Check if the list is empty
        raise ValueError("List is empty")

    return max(l)  # Use the built-in max function to find the maximum element

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```