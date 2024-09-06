```python
def smallest_change(arr):
    arr.sort()
    changes = abs(len(arr) - 2)
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            changes = changes + 1
    return changes
```

The function `smallest_change()` first sorts the input array, then calculates the number of changes required as the absolute difference between the length of the array and 2. The variable 'changes' is incremented each time a comparison indicates that an element is not the same as its preceding neighbour. The final result is the minimum number of changes required to make the array palindromic.