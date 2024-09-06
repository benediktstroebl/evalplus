```python
def can_arrange(arr):
    index = -1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            index = i
            break
    return index
```

The function `can_arrange` iterates through the list, comparing each element to the previous one. When an element smaller than the previous one is found, the function returns its index, indicating a possible arrangement. If no suitable element is found, the function returns -1.