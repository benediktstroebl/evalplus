```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(lst)  # Return the maximum element in the list


# Test the function
if __name__ == "__main__":
    print(max_element([1, 2, 3]))  # Expected output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
    try:
        print(max_element([]))  # Test with an empty list
    except ValueError as e:
        print(e)  # Expected output: List is empty
```

In this script, we define a function `max_element` that takes a list of integers as input and returns its maximum element. We also include a check for an empty list and raise a `ValueError` if the list is empty. Finally, we test the function with some examples.