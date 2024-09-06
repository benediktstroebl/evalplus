```python
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in its correct position in the sorted array.
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return False

    # If all elements are in their correct positions, we can obtain a non-decreasing array by shifting.
    return True
```

This approach checks if any number is not in its correct position in the non-decreasing sequence. If any element is not at the correct position, we return False immediately, as we cannot obtain a sorted array in this case. Otherwise, we shift all elements to the left to make it non-decreasing, and thus, return True. This algorithm has a time complexity of O(N) where N is the length of the input list.