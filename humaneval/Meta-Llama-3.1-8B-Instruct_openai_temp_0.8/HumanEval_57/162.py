```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            increasing = False
        if l[i] > l[i-1]:
            decreasing = False
    
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, the `monotonic` function takes a list of numbers as input. It initializes two flags, `increasing` and `decreasing`, to `True`. It then iterates over the list from the second element to the last element. If it finds an element that is smaller than the previous one, it sets `increasing` to `False`. If it finds an element that is larger than the previous one, it sets `decreasing` to `False`. Finally, it returns `True` if either `increasing` or `decreasing` is still `True`, and `False` otherwise.