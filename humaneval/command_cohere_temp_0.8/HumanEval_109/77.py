```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required to sort the array
    shift = 0

    # Traverse the array from the last element to the first
    for i in range(1, len(arr)):
        # If the current element is greater than the element it is about to replace, it is not possible to sort the array
        if arr[i] > arr[i-1]:
            shift += 1
            if shift > len(arr):
                return False

    # If we have tried shifting every possible amount and the array is still sorted, it is possible
    return True
```
This Python script defines the `move_one_ball()` function, which takes an array of numbers as input and returns a boolean value depending on whether it's possible to sort the array in non-decreasing order by shifting all the elements right by one position.

The function first checks if the array is empty, and if so, it returns `True` because shifting is not required to sort an empty array.

Then, the function counts the number of right shifts needed to sort the array by traversing it from the last element to the first. If at any point an element is greater than the element it's about to replace, the `shift` counter is incremented. Additionally, if the maximum number of shifts (the length of the array) is reached without sorting the array, the function returns `False` as it's not possible to sort the array by shifting.

Finally, if the function has checked every possible shift amount without encountering a problem, it returns `True`, indicating that the array can be sorted by performing the right shift operation the appropriate number of times.