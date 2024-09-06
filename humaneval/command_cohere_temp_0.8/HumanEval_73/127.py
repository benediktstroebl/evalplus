```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required
    """
    # Ensure the array contains only unique integers. This is the minimum number of changes
    changes = len(arr) - len(set(arr))
    
    # Ensure the array is a palindrome. This is the maximum number of changes
    mirror = [x for x in arr[::-1]]
    mirror_changes = len(mirror) - len(set(mirror))
    
    return min(changes, mirror_changes)
```

This function calculates the minimum number of changes required to make the array palindromic by taking into account two constraints:
1. The array must be made of unique elements (to handle repeats)
2. The array must be palindromic (read the same forwards and backwards)

The function returns the smallest of these two values, which represents the minimum number of changes required.