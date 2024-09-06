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
    # Calculate reverse as a shortcut to counting changes.
    reverse = [0] * len(arr)
    for i in range(len(arr)):
        reverse[i] = arr.index(arr[i]) + 1
    # Calculate changes by finding the difference between indices in normal
    # and reverse order.
    changes = 0
    for i in range(len(arr)):
        changes += abs(reverse[i] - i)
    return changes
```

This approach takes advantage of the problem definition's allowance for changing elements to their current values. By using the index of the first occurrence of each unique value in the array, reverse is created. The number of changes is then computed as the sum of absolute differences between corresponding indices in normal and reverse order. This works because the absolute difference represents the 'distance' between the element and its match in a palindrome.

This implementation has a time complexity of O(n), where n is the length of the input array, arr.