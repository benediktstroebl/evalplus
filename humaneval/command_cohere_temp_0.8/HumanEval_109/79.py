Here's a Python script that includes a function called `move_one_ball(arr)` that solves the problem you described:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and get the index of the last element
    arr.sort()
    last_idx = len(arr) - 1

    # Iterate through the sorted array and check for holes
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            return False

    # If the last element is not at the first index, there's a hole
    if arr[0] != arr[last_idx]:
        return False

    # If no holes found, the array can be sorted in non-decreasing order
    return True
```

This script provides a function that takes an array as input and returns `True` if the array can be sorted in non-decreasing order by moving one ball, and `False` otherwise. You can use this function to solve the problem you described. 

This solution assumes that the array will contain at least one element since an empty array is already considered sorted. Additionally, it assumes that the array elements are unique, as mentioned in the note in the problem statement.