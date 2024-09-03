```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindrommic array is a sequence that is read the same backwards and forwards.
    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # Sort the array
    arr.sort()

    = sorted(arr)
    n = len(arr)

    # Find the first and last elements in the sorted array
    first = n - 1
    last = 0

    # The number of changes needed is the absolute difference between the first and last elements
    # in the sorted array
    changes = abs(arr[first] - arr[last])

    # If the array is already palindromic, no changes are needed
    if changes == 0:
        return 0

    # The number of changes needed is equal to the number of elements in the array
    return n
```