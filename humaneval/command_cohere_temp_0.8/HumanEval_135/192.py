```python
def can_arrange(arr):
    prev = arr[0]
    arranges = []
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur <= prev:
            arranges.append(idx)
            prev = cur
    return max(arranges) if arranges else -1
```

The function uses a loop to iterate through the array, comparing each element to the previous one. If a larger element is encountered, it returns -1 indicating no arrangement possible. If an element smaller than or equal to the previous one is found, its index is added to the `arranges` list. Finally, it returns the maximum index of the elements that can be arranged, or -1 if none are found.