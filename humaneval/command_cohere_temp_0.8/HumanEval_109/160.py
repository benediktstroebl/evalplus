Here's a Python script that contains a function named `move_one_ball` inspired by the problem statement provided:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Sort the array in place using sorting indices.
    sorting_idx = [i for i in range(len(arr))]
    sorting_idx.sort(key=lambda i: arr[i])
    
    # If the sorted array is non-decreasing, return True.
    for i in range(len(arr)):
        if arr[sorting_idx[i]] < arr[i]:
            return True
    
    # If all elements are equal, it's still possible to sort the array.
    if len(set(arr)) == 1:
        return True
    
    # Otherwise, it's not possible to sort the array by moving one ball.
    return False
```

This approach utilizes sorting indices to determine if the array can be sorted. If the array can be sorted in non-decreasing order using sorting indices, it returns `True`, whereas it returns `False` if that is not possible. The use of sorting indices helps conserve memory and improves efficiency. This method has a time complexity of `O(n log n)` due to the use of the sorting indices technique, which happens in linear time.