```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if len(arr) == 0:
        return True

    # Check if the last element is the smallest and all other elements are greater
    if arr[-1] >= arr[0] and arr[0] <= arr[1]:
        return False

    # If the condition is not met, it is possible to sort by shifting
    return True
```

This script assumes that the input array `arr` is not empty, as the base case to return `True` is when the length of the array is zero. 

The script checks if the last element in the array is the smallest and if the first element is the largest. If this condition is not met, it returns `True`. If the condition is met, it checks if the first and last elements swap, resulting in the smallest-to-largest order. If this is not possible, it returns `False`. 

Note that this approach assumes that the array elements are unique.