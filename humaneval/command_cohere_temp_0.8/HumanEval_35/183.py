```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        raise ValueError("Input list is empty")

    max_element = max(l)
    return max_element
```

The Python function max_element takes a list l as input and returns the maximum element in the list. The function handles the case where the input list is empty, explicitly handling it with a ValueError. The max() function efficiently determines the maximum element, making this a concise and effective solution. The unit tests presented in the problem are adequate to cover the functionality of this solution.