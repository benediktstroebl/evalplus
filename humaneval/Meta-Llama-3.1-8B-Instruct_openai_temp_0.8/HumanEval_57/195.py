### Monotonic List Checker
#### Problem Description
This script defines a function `monotonic` that checks if a given list of numbers is monotonically increasing or decreasing.
#### Solution
```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing.
    """
    increasing = decreasing = True
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
#### Explanation
The `monotonic` function checks two conditions for the list: monotonic increasing and monotonic decreasing. It uses two flags, `increasing` and `decreasing`, initially set to `True`. It then iterates through the list, comparing each element with its predecessor. If it finds a pair where the current element is smaller than the previous one, it sets `increasing` to `False`. If it finds a pair where the current element is larger than the previous one, it sets `decreasing` to `False`. After the iteration, it returns `True` if either `increasing` or `decreasing` is still `True`, indicating that the list is either monotonically increasing or decreasing.