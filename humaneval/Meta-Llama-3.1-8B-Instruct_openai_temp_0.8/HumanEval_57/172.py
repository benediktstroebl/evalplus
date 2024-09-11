```markdown
### Monotonic List Checker

This script checks if the elements in a given list are monotonically increasing or decreasing.

```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    lst (list): A list of elements to check.

    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False

    return increasing or decreasing


# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, the `monotonic` function checks if the list elements are monotonically increasing or decreasing by comparing each element with its previous element. The `increasing` and `decreasing` flags are initially set to True. If the function encounters an element that is smaller than its previous element, it sets `increasing` to False. If it encounters an element that is larger than its previous element, it sets `decreasing` to False. Finally, it returns True if either `increasing` or `decreasing` is still True, indicating that the list elements are monotonically increasing or decreasing.