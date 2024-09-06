Here's a Python script with a self-contained function that solves the problem:
```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[::-1]):
        if a != b:
            changes += 1
    return changes
```
This script defines the `smallest_change` function, which takes an array `arr` as input and returns the smallest number of changes required to make the array palindromic. The function iterates through the array, checking each element against its corresponding element in the reversed array. If the elements match, it increments the changes counter. If they don't, it increments the counter by 1. Finally, it returns the changes counter.