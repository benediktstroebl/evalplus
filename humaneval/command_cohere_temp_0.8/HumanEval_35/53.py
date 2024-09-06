```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
The max_element function takes a list, l, as input and returns the maximum element in the list. The function uses the max function to compare and return the maximum value in the provided list. The type hint for the return type is int, following the convention that the max function returns an int value when applied to a list of integers.

The function includes examples in the docstring that demonstrate the behavior of the function. These examples are in the form of test cases since they show the input and expected output. The `max_element` function returns the expected output for the given input list `[1, 2, 3]` and `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]`. The string `3` and `123` are the expected results for the max element in the list, respectively.  These examples help to illustrate how the function behaves in different scenarios.