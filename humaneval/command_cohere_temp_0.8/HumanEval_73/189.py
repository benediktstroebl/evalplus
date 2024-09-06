Here's a Python script with a self-contained function that solves the problem using Python:
```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[1:][::-1]):
        if a != b:
            changes += 1
    return changes
```
This script defines the `smallest_change` function, which takes an array `arr` as input. It counts the number of changes needed to make the array palindromic by iterating through each element and its corresponding element in the reverse sequence. If the elements match, it increments the changes count. Otherwise, it increments the count by 1. Finally, it returns the changes count, which represents the minimum number of elements that need to be changed to make the array palindromic.