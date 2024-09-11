```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of numbers to be incremented.

    Returns:
        list: List with numbers incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Testing the function
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this script, we define a function `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. We use a list comprehension to create the new list. This is a concise and efficient way to create new lists in Python.

The function is then tested with the provided example inputs. The expected output is printed to the console for verification.