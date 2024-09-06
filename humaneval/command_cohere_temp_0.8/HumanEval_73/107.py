```python
def smallest_change(arr):
    changed = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changed += 1
    return changed
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of elements that need to be changed to make the array palindromic. The function uses a loop to iterate through the array and calculates the number of changes required by counting the number of times the corresponding elements do not match in reverse order. The result is the number of elements that need to be changed to make the array palindromic.