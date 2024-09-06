```python
def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        return None  # Return None if the list is empty

    max_el = l[0]  # Initialize the maximum element to the first element of the list

    for el in l:
        if el > max_el:
            max_el = el

    return max_el
```

The Python script defines a function `max_element` that finds the maximum element in a given list. It initializes the maximum element to the first list element and then iterates through the list, updating the maximum if a larger element is encountered. The function handles empty lists by returning `None`, and the docstring includes example tests.  This approach has a time complexity of O(n) since it requires iterating through the entire list once to find the maximum element.