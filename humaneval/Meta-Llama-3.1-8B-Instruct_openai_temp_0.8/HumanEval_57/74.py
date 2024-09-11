```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements.

    Returns:
        bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False

    return increasing or decreasing


# Example use cases:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. The function iterates over the list and checks if each element is greater than or less than its previous element. If it finds an element that is both greater and less than its previous element, it concludes that the list is not monotonically increasing or decreasing. The function returns True if the list is monotonically increasing or decreasing, and False otherwise. The example use cases demonstrate the function's usage.