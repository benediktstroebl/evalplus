```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Calculate the list of changes required to make the array palindromic
    changes = []
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            changes.append(1)
        else:
            changes.append(0)
    # Return the minimum number of changes
    return min(changes)
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic.

The approach is as follows:
1. Ensure the array contains only unique integers using set(arr).
2. Calculate the list of changes required to make the array palindromic, iterating through the array and comparing each element with the previous one.
3. Return the minimum number of changes from the changes list.

This solution adheres to the problem guidelines, finding the minimum number of changes required to make the array palindromic, with each change allowing the modification of a single element into any other element.