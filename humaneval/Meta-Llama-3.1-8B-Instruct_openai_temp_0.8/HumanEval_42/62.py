```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list containing integers.

    Returns:
        list: The input list with elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we define a function `incr_list` that takes a list of integers as input and returns a new list with the same elements incremented by 1. The function uses a list comprehension to create a new list where each element is the corresponding element in the input list incremented by 1. The test cases are included at the end of the script to verify that the function works as expected.