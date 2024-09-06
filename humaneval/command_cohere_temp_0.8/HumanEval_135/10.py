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
    return -1 if idx == len(arr) else idx
```
The function `can_arrange` iterates through the list `arr`, comparing each element to the previous one. If an element is smaller than the previous one, the function increments the index and breaks the loop. If the loop completes without breaking, meaning all elements are greater or equal to the previous one, the function returns -1. Otherwise, it returns the largest index of the element that broke the loop.