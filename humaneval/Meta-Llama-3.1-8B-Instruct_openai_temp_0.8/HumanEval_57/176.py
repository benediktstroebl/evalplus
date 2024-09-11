```python
def monotonic(l: list):
    """
    Return True is list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of numbers.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True

    # Check if the list is empty
    if len(l) > 1:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                increasing = False
            if l[i] > l[i - 1]:
                decreasing = False

        return increasing or decreasing

    return True  # If the list contains one or zero elements, it's considered monotonic

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([4]))  # True
print(monotonic([]))  # True
```