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
        if lst[i] > lst[i + 1]:
            increasing = False
        if lst[i] < lst[i + 1]:
            decreasing = False

    return increasing or decreasing


# Test cases
if monotonic([1, 2, 4, 20]):
    print("Test case 1 passed")
if not monotonic([1, 20, 4, 10]):
    print("Test case 2 passed")
if monotonic([4, 1, 0, -10]):
    print("Test case 3 passed")
```

This script defines a function `monotonic` that checks if a list of numbers is monotonically increasing, decreasing, or neither. It then tests the function with the provided test cases. The function uses two flags: `increasing` and `decreasing`, which are initially set to `True`. It then iterates over the list, updating these flags whenever it encounters a pair of elements that are not monotonically related. Finally, it returns `True` if either flag is still `True`, indicating that the list is monotonically increasing or decreasing.