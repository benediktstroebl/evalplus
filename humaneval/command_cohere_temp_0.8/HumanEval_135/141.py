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

The function `can_arrange()` iterates through the array, comparing each element to the previous one. If an element is greater than or equal to the previous one, it returns -1 immediately since it cannot be the answer. If, on the other hand, the element is smaller than the previous one, it updates the answer accordingly. Finally, it returns the largest index of such elements, or -1 if none are found. 

This approach ensures that the function considers all elements of the array while maintaining efficiency.