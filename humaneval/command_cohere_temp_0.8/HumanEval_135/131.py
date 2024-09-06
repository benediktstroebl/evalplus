```python
def can_arrange(arr):
    prev = arr[0]
    arranged = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        arranged = idx
        break
    else:
        return -1
    return arranged
```

The function `can_arrange()` iterates through the array, comparing each element to the previous one. When an element greater than the previous one is found, the function returns its index. If no such element is found, meaning the array is sorted or reversed, it returns -1.