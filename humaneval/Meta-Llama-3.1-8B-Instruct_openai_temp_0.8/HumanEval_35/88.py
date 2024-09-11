### Finding Maximum Element in a List

Here's a simple Python function that finds the maximum element in a list:

```python
def max_element(l: list):
    """Return maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")

    # Use built-in max function to find the maximum element
    return max(l)
```

You can use this function as follows:

```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This function uses Python's built-in `max` function, which returns the largest item in an iterable (like a list). It also includes a check for an empty list to raise a `ValueError` if the list is empty.