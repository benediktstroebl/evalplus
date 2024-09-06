```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes required to make the array palindromic.
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Sort the array
    sorted_arr = sorted(arr)
    # Get the number of elements at the start and end of the array
    left, right = sorted_arr[:len(arr) // 2], sorted_arr[len(arr) // 2 :]
    # Count the number of elements that are not common between start and end
    return len(left) + len(right) - max(len(left), len(right))
```

The function first converts the array to a set to remove any duplicate elements, as having duplicate elements does not impact the problem's solution. The array is then sorted, and the length of the array at the start and end of the sorted array are extracted. These are `left` and `right`, respectively.

The function then calculates the maximum length between `left` and `right` and subtracts this from the total length of `left` and `right` to determine the minimum number of changes required to make the original array palindromic.

This approach takes advantage of the fact that any palindromic array must have symmetrical elements at the start and end, and the number of changes is dependent on the elements at the start and end that are not symmetrical.