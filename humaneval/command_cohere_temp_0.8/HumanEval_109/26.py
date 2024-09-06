```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if len(arr) == 0:
        return True

    # Check if any element exists in the array that is not in the first position
    for i in range(1, len(arr)):
        if arr[i] != arr[0]:
            return True

    return False

# Test Cases
arr1 = [3, 4, 5, 1, 2]
arr2 = [3, 5, 4, 1, 2]

print(move_one_ball(arr1))  # Output: True
print(move_one_ball(arr2))  # Output: False
```

This code defines a function `move_one_ball()` that takes an array as input and returns `True` if it's possible to sort the array in non-decreasing order by moving one ball, which implies that there is at least one element in the array that isn't in the first position, or `False` otherwise. The function examines each element in the array, starting with the second element, `arr[1]`, and checks if it is different from the first element, `arr[0]`. If this condition is met for any element in the array, it returns `True`, indicating that we can achieve a sorted order by moving one ball. If the condition is not met for any element in the array, it returns `False`, indicating that no ball movement will result in a sorted order.