```python
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in its correct position in the sorted array.
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return False

    return True
```

This function checks whether it's possible to sort the array in non-decreasing order by shifting all the elements one position to the right. It examines each element in the array and determines if it's in its correct position in a sorted array. If any element is not at its correct position, the function returns False, indicating that a non-decreasing sorted array cannot be formed through right shifts. If all elements are in their correct positions, the function returns True. Additionally, the function handles the edge case where the array is empty, returning True since an empty array can be sorted in any order.