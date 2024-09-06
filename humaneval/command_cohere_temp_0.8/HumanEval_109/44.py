Here's a Python script that contains a function named `move_one_ball` that solves the problem you've described:
```python
def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    m = arr[0]
    for i in range(1, n):
        if m > arr[i]:
            return False
        m = arr[i]
    return True
```

This function checks if the last element in the array is the largest. If it is, it iterates over the array from index 1 to the second last index, comparing the current element to the last element. If any element is larger than the last element, it returns `False` since doing a right shift operation will not lead to a non-decreasing array. However, if the loop completes without finding a larger element, it means the array is already in non-decreasing order, and the function returns `True`. 

is possible to sort the array in non-decreasing order by performing right shift operations.