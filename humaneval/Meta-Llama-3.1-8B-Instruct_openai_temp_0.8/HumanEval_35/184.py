```python
def max_element(l: list) -> int:
    """
    Return the maximum element in the list.
    
    Args:
    l (list): A list of elements.
    
    Returns:
    int: The maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")

    # Use built-in max function to find the maximum element in the list
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list of elements as input and returns the maximum element in the list. It uses the built-in `max` function to achieve this. If the input list is empty, it raises a `ValueError`. The script also includes two test cases to demonstrate the function's behavior.