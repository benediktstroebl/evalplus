```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False

    return increasing or decreasing


# Example use cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

However, a more Pythonic and efficient way to solve this problem would be to use the `all()` function with a generator expression:

```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(x <= y for x, y in zip(lst, lst[1:])) or all(x >= y for x, y in zip(lst, lst[1:]))


# Example use cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This version of the function works by checking if all pairs of adjacent elements in the list are either less than or equal to each other (for increasing) or greater than or equal to each other (for decreasing). If either condition is true, the function returns `True`; otherwise, it returns `False`.