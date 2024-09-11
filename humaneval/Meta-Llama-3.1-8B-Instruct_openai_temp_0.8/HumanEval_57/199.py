```python
def monotonic(lst: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing."""
    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False

    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

In this script, the function `monotonic` checks if the list elements are monotonically increasing or decreasing. It maintains two flags, `increasing` and `decreasing`, initially set to `True`. If at any point it finds an element that is less than its previous element, it sets `increasing` to `False`. Similarly, if it finds an element that is greater than its previous element, it sets `decreasing` to `False`. At the end of the function, it returns `True` if either `increasing` or `decreasing` is still `True`, meaning the list elements are monotonically increasing or decreasing.