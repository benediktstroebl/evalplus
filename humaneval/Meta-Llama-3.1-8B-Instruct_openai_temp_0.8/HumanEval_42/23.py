```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of integers.

    Returns:
        list: A new list containing the incremented elements.

    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script:

- We define a function `incr_list` that takes a list `l` as an argument.
- The function uses a list comprehension to create a new list where each element is incremented by 1.
- We include docstrings to explain what the function does, its parameters, and its return value.
- We test the function with the provided example inputs.