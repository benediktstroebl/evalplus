```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changes += 1
    return changes
```

The function iterates through the array and compares each element to its corresponding element in the reversed sequence using the `zip` function. When an element mismatch is encountered, the `changes` counter is incremented. Finally, the total count is returned, representing the minimum number of changes required to make the array palindromic.

This approach has a time complexity of O(n), where 'n' is the length of the input array, as it requires iterating through each element once.