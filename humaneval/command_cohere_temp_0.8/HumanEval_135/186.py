```python
def can_arrange(arr):
    prev = arr[0]
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            continue
        else:
            idx = i + 1
            break
    return arr[idx] if idx < len(arr) and arr[idx] > prev else -1
```

The function iterates through the array, comparing each element to the previous one. If an element is smaller than the previous one, it keeps track of the index and breaks out of the loop. If no suitable element is found after iterating through the array, it returns -1. Otherwise, it returns the index of the first suitable element, ensuring the largest index of an element that fits the criteria is returned.