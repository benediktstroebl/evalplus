```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of integers.

    Returns:
        list: List with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]


# Example usage:
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

In this code, the `incr_list` function uses a list comprehension to create a new list where each element is incremented by 1. The `i + 1` expression is applied to each element `i` in the input list `l`. The resulting list is then returned by the function. The example usage at the end demonstrates how to call the `incr_list` function with different input lists and print the resulting lists.