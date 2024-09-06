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

    max_el = l[0]
    for num in l:
        if num > max_el:
            max_el = num
    return max_el
```

The given Python script provides a function named `max_element` that accepts a list `l` as an argument and returns the maximum element present in the list. The function initially verifies whether the list is empty; if so, it returns `None`. If the list contains elements, the function initializes a variable `max_el` with the first element of the list and then iterates through the list, updating `max_el` with a larger value if encountered. The function ultimately returns the maximum element found in the list.

The script includes example tests in the comment section, demonstrating how the function effectively computes and returns the maximum element in two different lists.