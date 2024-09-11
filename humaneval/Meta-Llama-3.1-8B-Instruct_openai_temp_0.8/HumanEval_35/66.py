```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        raise ValueError("List is empty")
    else:
        return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list `l` as input and returns the maximum element in the list. It uses the built-in `max` function in Python to find the maximum element.

If the input list is empty, it raises a `ValueError` with a message indicating that the list is empty.

The script also includes test cases to demonstrate the function's behavior.