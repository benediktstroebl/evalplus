### Monotonic List Checker

Here is a Python script that implements a function to check if a list is monotonically increasing or decreasing:

```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The list to check.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(lst)):
        # Check if the list is increasing
        if lst[i] < lst[i - 1]:
            increasing = False
        # Check if the list is decreasing
        if lst[i] > lst[i - 1]:
            decreasing = False

    # The list is monotonically increasing or decreasing if and only if one of the conditions is still True
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The function iterates through the list and checks if the list is increasing or decreasing by comparing each element with its previous element. If it finds an element that is smaller than the previous one, it sets the `increasing` flag to `False`. Similarly, if it finds an element that is larger than the previous one, it sets the `decreasing` flag to `False`. Finally, it returns `True` if and only if one of the conditions is still `True`, indicating that the list is monotonically increasing or decreasing. The script also includes test cases to verify the correctness of the function.