```python
def can_arrange(arr):
    result = -1
    for idx, value in enumerate(arr):
        if value > arr[idx-1]:
            result = idx
    return result
```
The function `can_arrange` iterates through the array, comparing each element to the preceding one, and returns the largest index of an element that is not greater than or equal to the previous element. If no such element exists, it returns -1. Feel free to test this code with different input arrays to verify its behavior.