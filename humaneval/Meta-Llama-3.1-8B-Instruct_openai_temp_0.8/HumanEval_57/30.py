### Monotonically Increasing or Decreasing List Check
```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The list to check.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        elif lst[i] < lst[i - 1]:
            increasing = False

    return increasing or decreasing


# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
This script defines a function `monotonic` that takes a list as input and returns `True` if the list elements are monotonically increasing or decreasing. The function uses two flags `increasing` and `decreasing` to track whether the list is increasing or decreasing. It then iterates over the list and sets the flags accordingly. Finally, it returns `True` if either flag is `True`, indicating that the list is monotonically increasing or decreasing.