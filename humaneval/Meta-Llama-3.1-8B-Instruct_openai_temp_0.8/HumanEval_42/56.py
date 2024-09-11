```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of integers.

    Returns:
        list: List of integers incremented by 1.
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This Python script defines a function `incr_list` that takes a list of integers as input and returns a new list where each element is incremented by 1. It uses a list comprehension to create the new list. The test cases at the end demonstrate the function's usage and expected output.