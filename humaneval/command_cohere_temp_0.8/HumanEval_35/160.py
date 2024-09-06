```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
```
This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. Inside the function, the `max` built-in function is used to determine the maximum value in the list.

The function is tested twice in the docstring with inline pytest assertions. In the first test, the maximum element in the list `[1, 2, 3]` is expected to be `3`. In the second test, the maximum element in the list `[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]` is expected to be `123`.

This code is an efficient and straightforward solution to finding the maximum element in a list, as it leverages Python's built-in `max` function to perform the operation in O(n) time complexity, where n is the number of elements in the input list.