```python
def can_arrange(arr):
    prev = arr[0]
    max_index = -1
    
    for i in range(1, len(arr)):
        if arr[i] >= prev:
            max_index = i 
        prev = arr[i]
    
    return max_index
```
The `can_arrange` function iterates over the array, comparing each element to the previous one. If the element is greater than or equal to the previous one, the `max_index` is updated to the current index, and the loop continues. If no suitable element is found, the function returns -1.  This approach ensures that `max_index` always holds the largest index of an element that satisfies the given condition.