```python
def can_arrange(arr):
    prev = arr[0]
    ans = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur < prev:
            ans = idx
        prev = cur
    return ans
```

The function `can_arrange()` iterates over the entire array, comparing each element to the previous one. If a larger element is found, the function returns -1 immediately, indicating that no suitable element is found. If the loop completes without encountering any larger element, the current index is the largest index of the desired element, and this value is returned.