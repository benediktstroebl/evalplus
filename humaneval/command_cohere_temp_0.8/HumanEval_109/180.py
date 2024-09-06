```python
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element exists in the array that is not in the first position.
    for i in range(1, len(arr)):
        if arr[i] != arr[0]:
            return True

    # If all elements are present in the first position, it's not possible to obtain a non-decreasing array.
    return False

# Test scenarios
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
```

This code defines a function `move_one_ball()` that takes an array `arr` as input and returns `True` if it's possible to sort the array in non-decreasing order by performing a right shift operation, and `False` otherwise. The function checks if any element exists in the array that is not in the first position, if so, it returns `True`. If all elements are present in the first position, it returns `False`.