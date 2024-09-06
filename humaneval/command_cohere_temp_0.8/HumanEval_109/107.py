```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in the first half of the array.
    index = arr[-1]
    left = 0
    for i in range(len(arr)):
        if arr[i] < index:
            left += 1
        if left > len(arr) // 2:
            return False

    return True
```

This Python script defines the `move_one_ball()` function, which takes an array `arr` as input. The function returns `True` if it's possible to sort the array in non-decreasing order by moving one ball (performing a right shift operation), and `False` otherwise. It checks if the last element in the array is present in the first half or not by traversing the array. If it finds any element less than the last element in the first half, it returns `True`. If it reaches the end without finding any such element, it returns `False`. The script returns `True` if the array is empty.  The approach has a time complexity of `O(n)`, where `n` is the length of the array, as it requires traversing the entire array once.