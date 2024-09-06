```python
def max_element(l: list):
    """Return maximum element in the list.

    :param l: A list of numbers.
    :type l: list
    :return: The maximum element in the list.
    :rtype: int or float
    """
    if not l:
        raise ValueError("Input list is empty")
    max_el = max(l)
    return max_el
```

The function employs the built-in `max` function to find the maximum value in the input list. It is important to note that the function initially checks if the input list is empty, and if so, raises a `ValueError` to handle this case.