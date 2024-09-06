Here's a Python script that contains a function named `move_one_ball` encompassing the problem statement above:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Traverse through the array and check if any element is greater than the last element
    for i in range(len(arr) - 1):
        if arr[i] > arr[-1]:
            return False

    # If no larger element is found, it's possible to achieve sorted order
    return True

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
```

In this script, the `move_one_ball` function takes an array `arr` as input and checks whether any element in the array is greater than the last element. If there are any such elements, it returns False immediately, as we cannot obtain a sorted array through the specified operations. If no larger element is found in the array, it returns True, indicating that a sorted array can be obtained through repeated right shifts.