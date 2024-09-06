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
    max_el = l[0]
    for num in l:
        if num > max_el:
            max_el = num
    return max_el
```

The given Python script provides a self-contained function called `max_element()` that finds the maximum element in a given list. It initially checks if the list is empty, in which case it returns `None`. If the list contains elements, the function iterates through the list, comparing each element to the current maximum element stored in the variable `max_el`. It updates `max_el` whenever it finds an element greater than the previous maximum. The function ultimately returns the maximum element found in the list.

This solution includes a docstring that explains the purpose of the function and provides example tests in the format of Python's built-in `assert` statements. These tests demonstrate the function's behavior on two example lists, confirming that it returns the correct maximum elements.