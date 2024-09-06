```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changes += 1
    return changes
```

The function `smallest_change` takes an array `arr` as input and returns the smallest number of changes required to make the array palindromic. The function counts the number of changes by iterating through the array and its reversed counterpart, using the `zip` function. When a pair of elements do not match, a change is counted. The result is the total count of changes needed.