### Monotonic List Checker
```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The input list to check.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False
        if l[i] > l[i - 1]:
            decreasing = False

    return increasing or decreasing


# Example use cases
if __name__ == "__main__":
    print(monotonic([1, 2, 4, 20]))  # True
    print(monotonic([1, 20, 4, 10]))  # False
    print(monotonic([4, 1, 0, -10]))  # True
```
This script defines a function `monotonic` that takes a list as input and returns `True` if the list elements are either monotonically increasing or decreasing, and `False` otherwise. The function uses two boolean variables `increasing` and `decreasing` to track whether the list is increasing or decreasing, respectively. It then iterates over the list, updating these variables as it goes. Finally, it returns `True` if either `increasing` or `decreasing` is `True`, and `False` otherwise.