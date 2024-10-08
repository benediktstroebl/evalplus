```python
def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur >= prev:
            continue
        max_idx = idx
        prev = cur
    return max_idx
```

The function `can_arrange` takes an array `arr` as input and returns the largest index of an element that is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1. The provided example arrays demonstrate how the function works.