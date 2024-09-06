```python
def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for idx, cur in enumerate(arr[1:]):
        if cur > prev:
            continue
        elif cur < prev:
            ans = idx + 1
        else:
            prev = cur
    return max(ans, -1)
```

The function `can_arrange()` iterates through the array, comparing each element to the previous one. If a larger element is found, it continues to the next element. If a smaller element is found, the answer is changed to the current index plus 1. If the element is equal, then the previous element is updated to the current element, and the process continues. The maximum index is returned unless the answer is -1, in which case the index will be undefined or unreliable, and -1 is returned as a warning. This algorithm is not the most efficient solution (LOL). It has a time complexity of O(n^2) but easiy to understand and simulate in your head.