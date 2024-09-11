```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): List of elements
    
    Returns:
        The maximum element in the list
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("List is empty")
    max_val = l[0]
    for elem in l:
        if elem > max_val:
            max_val = elem
    return max_val

# Test cases
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
try:
    print(max_element([]))  # Expected output: ValueError
except ValueError as e:
    print(e)

```

This script defines a function `max_element` that takes a list of elements as input and returns the maximum element. It first checks if the list is empty, in which case it raises a `ValueError`. Otherwise, it iterates over the list to find the maximum element. The test cases demonstrate the function's behavior with a non-empty list, an empty list, and a list with negative numbers.