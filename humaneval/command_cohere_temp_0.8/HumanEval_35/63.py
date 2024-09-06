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

    max_el = l[0]  # Initialize max_el to the first element of the list

    for el in l:
        if el > max_el:
            max_el = el

    return max_el
```

The script initializes the max_el variable to the first element of the input list. It then iterates over the list, comparing each element to max_el, and updates max_el if a larger element is encountered. If the list is empty, it returns None. This ensures an efficient and elegant solution to finding the maximum element in a list, as testified by the test cases provided in the prompt.