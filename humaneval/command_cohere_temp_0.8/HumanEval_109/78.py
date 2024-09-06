```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Sort the array and remove duplicates.
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Check if the sorted array can be created by shifting elements to the left.
    for i in range(len(arr)-1):
        if sorted_arr[i] != arr[i+1]:
            return False

    return True
```

The reasoning behind the approach is to first check if the array is empty, which is a special case that can be sorted in non-decreasing order. If the array is not empty, we then sort the array and remove any duplicates, and then check if the sorted array can be created by shifting elements from the original array one position to the left. If any element at index `i` in the original array does not match the element at index `i+1` in the sorted array, then it is not possible to achieve a non-decreasing order, and the function returns `False`. If all elements match, then it is possible to achieve a non-decreasing order by shifting all elements to the left, and the function returns `True`. 

This approach optimally solves the problem in a straightforward manner, making it a clean and efficient implementation.