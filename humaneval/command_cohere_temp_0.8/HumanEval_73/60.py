```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changes += 1
    return changes
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of changes required to make the array palindromic. The function uses a for loop to iterate through each pair of elements in the array and its reverse, checking if they are different, and incrementing the changes count for each difference. The final count of changes is returned.

This approach has a time complexity of O(n^2) due to the pairwise comparison of elements in the array and its reverse. It is efficient and works for any input array.