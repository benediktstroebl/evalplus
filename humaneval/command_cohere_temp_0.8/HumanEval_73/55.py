```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required.
    """
    # Ensure the array contains only unique integers.
    arr = list(set(arr))
    # Sort the array.
    arr.sort()
    # Count duplicates.
    dup_count = arr[::-1].count(arr)
    # Return the minimum of zero, dup_count, and len(arr) - dup_count.
    return min(dup_count, len(arr) - dup_count, 0)
```

The function works by first removing any duplicate elements from the array, as they do not contribute to the problem. It then sorts the array, so that the elements to be changed are clearly defined. The code then counts the number of elements in the array that are present in the reverse of the array. This gives an upper bound on the number of elements that need to be changed, assuming each change turns an element into its reverse. 

Then, to find the minimum number of changes required, the function returns the smaller of three values: `dup_count`, `len(arr) - dup_count`, and zero, each of which represents a scenario where all elements are unique, all elements are duplicates, and half of the elements are reversed respectively.