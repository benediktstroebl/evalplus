Here's a Python script with a self-contained function that solves the problem using Python:
```python
def smallest_change(arr):
    changes = 0
    for a, b in zip(arr, arr[::-1]):
        if a != b:
            changes += 1
    return changes
```
This script defines the `smallest_change` function, which takes an array `arr` as input and returns the minimum number of elements that need to be changed to make the array palindromic. The function uses a `for` loop to iterate through the array, and checks each element against its corresponding element in the reversed array. If the elements do not match, then one change is counted for the two elements. The loop counts the number of differences between the forward and reversed array, which is then returned as the result.