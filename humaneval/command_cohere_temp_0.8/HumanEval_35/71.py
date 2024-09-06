```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    max_el = max(l)
    return max_el
```
The function `max_element` returns the maximum element in the list. It first checks if the list is empty, in which case it returns `None`. If the list is not empty, it finds the maximum element using the `max` function and returns it. This approach ensures the function is resilient against empty lists and returns the maximum element for non-empty lists.  It allows the function to handle various scenarios effectively, passing the included tests.