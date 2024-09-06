```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            max_idx = i+1
            break
    return max_idx
```

The function `can_arrange` iterates over the array, and for each index, it compares the current element with the next one. If the current element is greater than the next one, this means that it can be rearranged, and the function returns the current index plus one. The loop continues until a valid index is found or the end of the array is reached. The initial value of `max_idx` is set to -1, and it is updated whenever a valid index is found. 

Here is an example usage of the function:
```python
arr = [1, 2, 4, 3, 5]
print(can_arrange(arr))  # Output: 3

arr = [1, 2, 3]
print(can_arrange(arr))  # Output: -1
```

The provided examples showcase how the function works correctly, returning the largest index of an element that can be rearranged within the given arrays.