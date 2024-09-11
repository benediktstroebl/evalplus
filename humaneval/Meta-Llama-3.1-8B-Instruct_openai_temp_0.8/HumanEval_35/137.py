```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This Python script defines a function called `max_element` that takes a list as input and returns the maximum element in the list. The function uses Python's built-in `max` function, which returns the largest item in an iterable or the largest of two or more arguments.

The script includes two test cases to verify that the function works correctly. The first test case checks that the function returns the maximum element from a list of small integers, and the second test case checks that the function returns the maximum element from a list of larger integers.