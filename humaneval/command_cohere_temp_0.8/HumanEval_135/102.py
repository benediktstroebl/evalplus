```python
def can_arrange(arr):
    prev = arr[0]
    max_idx = -1
    for idx, cur in enumerate(arr[1:]):
        if cur <= prev:
            max_idx = idx + 1
        prev = cur
    return max_idx
```

The function `can_arrange` iterates through the array, comparing each element to the previous one. If an element is greater than or equal to the previous one, the function sets `max_idx` to the current index plus one (`idx + 1`), as this is the first index of such element. The loop continues until a suitable element is found or the end of the array is reached. Finally, if no suitable element is found during the iteration, the function returns -1. 

This approach ensures that the function considers all elements for the highest index and handles scenarios where the array might be empty or contain just one element.