```python
def move_one_ball(arr):
    # if the array is empty, it is always possible to obtain a sorted array
    if not arr:
        return True

    # sort the array
    arr.sort()

    # when the sorted array has elements arranged in non-increasing order, it is possible to obtain a non-decreasing order with right shifts
    if arr[0] >= arr[1]:
        return True

    return False
```

The solution works by first checking if the array is empty, and if so, it returns True since shifting operations will not affect the order of the elements anyway. If the array is not empty, it sorts the array in non-increasing order using the sort() method. Then it checks if the first element of the sorted array is greater or equal to the second element. If this is the case, it returns True, as the sorted array already has elements in non-decreasing order, or could be achieved by performing a single right shift operation. Otherwise, it returns False.