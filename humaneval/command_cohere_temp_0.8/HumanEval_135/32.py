```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            arranged = i - 1
            break
        prev = arr[i]
    return arranged
```

The function `can_arrange` iterates through the array, comparing each element to its previous one, and keeps track of the largest index of an element that is not greater than or equal to the previous one. If no such element is found, it returns -1.