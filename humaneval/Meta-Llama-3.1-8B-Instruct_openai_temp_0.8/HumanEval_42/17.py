```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of integers.

    Returns:
        list: List with elements incremented by 1.
    """
    # Use a list comprehension to create a new list with elements incremented by 1
    return [x + 1 for x in l]

# Test cases
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines the `incr_list` function, which takes a list of integers as input and returns a new list with each element incremented by 1. The function uses a list comprehension to create the new list, which is more concise and efficient than using a for loop. The test cases at the end demonstrate the function's behavior with different inputs.