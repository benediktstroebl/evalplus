```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changes += 1
    return changes
```

The function `smallest_change` takes an array `arr` as input and returns the smallest number of changes required to make the array palindromic. The function uses a for loop to iterate through each pair of elements in the array and its reverse, checking if they are different, and incrementing the changes counter if they are. After iterating through all possible elements, the function returns the changes counter.

This solution does not use any additional libraries and can therefore be run as a standalone Python script.