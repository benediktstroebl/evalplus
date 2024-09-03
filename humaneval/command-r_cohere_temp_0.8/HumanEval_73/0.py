```python
def smallest_change(arr):
    """
    Finds the minimum number of elements to change to make the array palindromic.

    Args:
        arr (list): An array of integers.

    Returns:
        int: The minimum number of elements that need to be changed.
    """
    # O(n) time, O(n) space, where n is the length of arr
    n = len(arr)
    left, right = 0, n - 1
    changes = 0

    while left < right:
        if arr[left] != arr[right]:
            changes += 1
            left += 1
            right -= 1
        else:
            left += 1
            right -= 1

    return changes
```