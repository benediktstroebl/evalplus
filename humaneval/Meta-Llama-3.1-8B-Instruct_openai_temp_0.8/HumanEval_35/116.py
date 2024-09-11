```python
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        raise ValueError("List is empty")
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
print(max_element([]))  # Expected output: ValueError
```

In this script, the `max_element` function takes a list `l` as input and returns its maximum element. It raises a `ValueError` if the input list is empty, as the `max` function cannot find the maximum element in an empty list. The script also includes some test cases to demonstrate the function's behavior.