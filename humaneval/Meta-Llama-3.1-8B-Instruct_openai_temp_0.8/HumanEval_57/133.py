```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

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


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic(l)` that checks if the elements of the input list `l` are monotonically increasing or decreasing. It then tests this function using the provided test cases. The function works by initializing two flags, `increasing` and `decreasing`, to True and then iterating over the list from the second element to the end. If it finds any pair of elements where the first is greater than the second, it sets `increasing` to False. If it finds any pair of elements where the first is less than the second, it sets `decreasing` to False. Finally, it returns True if either `increasing` or `decreasing` is still True, indicating that the list is either strictly increasing or strictly decreasing.