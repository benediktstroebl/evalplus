```python
def smallest_change(arr):
    changed = 0
    for a, b in zip(arr, arr[::-1]):
        if a != b:
            changed += 1
    return changed
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of elements that need to be changed to make the array palindromic. The function uses a for loop to iterate through each element of the array and checks if the element matches its counterpart in the reverse sequence. If they don't match, the element is considered as a change, the `changed` counter is incremented by 1. Finally, the function returns the changed counter.

This solution does not require any additional libraries.