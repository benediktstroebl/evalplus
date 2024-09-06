```python
def move_one_ball(arr):
    # if the array is empty, it is always possible to obtain a sorted array
    if len(arr) == 0:
        return True
    # store the maximum and minimum value of the array
    maxx = max(arr)
    minn = min(arr)
    # if the difference between the maximum and minimum value of the array is equal to the length of the array, it is possible to obtain a sorted array by performing the right shift operation
    return maxx - minn == len(arr)
```