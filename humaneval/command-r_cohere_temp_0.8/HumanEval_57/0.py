```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    Args:
        l (list): Target list to check for monotonic properties.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check for special case of empty list
    if len(l) == 0:
        return False

    # Check for increasing monotonicity
    if l[0] <= l[1]:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                return False
        return True

    # Check for decreasing monotonicity
    return all(l[i] >= l[i - 1] for i in range(1, len(l)))
```