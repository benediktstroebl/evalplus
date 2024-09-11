```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        elif lst[i] > lst[i + 1]:
            increasing = False

    return increasing or decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # False
print(monotonic([1, 1, 1, 1, 1]))  # True
```