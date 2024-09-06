```python
def can_arrange(arr):
    prev = arr[0]
    arranged = 0
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return -1
        elif cur >= prev:
            arranged = idx
        prev = cur
    return arranged
```

The function `can_arrange()` iterates through the array, comparing each element to the previous one. If an element is greater than the previous one, the function returns -1 indicating that no suitable element is found. Otherwise, the function updates the `arranged` index and checks if the current element is not greater than or equal to the previous one. The loop continues until a suitable element is found, and its index is returned. 

**NOTE**: This approach is not optimized for large arrays or repeated elements, as it uses a linear search and compares each element to its previous one. Thus, the complexity remains O(n). For improved performance on such scenarios, consider using sorting algorithms like binary or radix sort to reduce unnecessary comparisons.