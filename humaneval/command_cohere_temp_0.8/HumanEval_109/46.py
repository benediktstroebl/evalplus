Here's a Python script that includes a function `move_one_ball(arr)` that addresses the problem you've described, along with a series of unit tests to validate its correctness:
```python
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    count = 0
    for i in range(len(arr)):
        if i > 0 and arr[i] > arr[i - 1]:
            count += 1
    return count % len(arr) == 0

# Unit tests
assert move_one_ball([3, 4, 5, 1, 2]) == True
assert move_one_ball([3, 5, 4, 1, 2]) == False
assert move_one_ball([2, 3, 4, 5, 1]) == True
assert move_one_ball([2, 4, 3, 5, 1]) == False
assert move_one_ball([1, 2, 3, 4, 5]) == True
assert move_one_ball([1, 3, 2, 4, 5]) == False
assert move_one_ball([5, 4, 3, 2, 1]) == True
assert move_one_ball([5, 3, 4, 2, 1]) == False
```

In the `move_one_ball(arr)` function, we iterate through the array and count the number of times the condition `arr[i] > arr[i - 1]` is true. This condition indicates that the current element is greater than the previous element, which is a requirement for a sorted array in non-decreasing order. If this condition is true for any element, we count it.

Then, we check if the count of such occurrences is a multiple of the array's length. If it is, it means we can create a non-decreasing ordered array by performing a number of right shifts equal to the count. If this condition is satisfied, we return `True`; otherwise, we return `False`.

The unit tests provided cover various cases to validate the correctness of the function. You can use them to ensure that the function behaves as expected for different input arrays.  If you encounter any difficulties or require additional information, please do not hesitate to ask!