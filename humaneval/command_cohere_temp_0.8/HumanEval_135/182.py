```python
def can_arrange(arr):
    prev = arr[0]
    mx = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur >= prev:
            return -1
        if cur > mx:
            mx = cur
        prev = cur
    return idx if mx != arr[idx] else -1
```

The function iterates through the array, comparing each element to the one before it, updating the maximum element found, and checking if it's eligible to be the answer (i.e., if the same element appears again, it's not eligible). If no eligible element is found, it returns -1. Otherwise, it returns the index of the eligible element. The function is designed to work with arrays that don't have duplicate values.