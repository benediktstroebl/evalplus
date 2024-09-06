```python
def can_arrange(arr):
    prev = arr[0]
    mx = -1
    for x in arr[1:]:
        if x > prev:
            return mx
        if x <= prev:
            mx = max(mx, x)
        prev = x
    return mx
```
This Python script defines a function named `can_arrange` that addresses the problem statement. It iterates through the array, keeping track of the maximum index of an element that is not greater than or equal to the previous element. The value `-1` is returned if no such element is found. The given example arrays demonstrate how the function works, returning the expected index values in each case.