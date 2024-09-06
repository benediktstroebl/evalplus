Here's a Python script that includes a function named `move_one_ball` with the specified behavior:
```python
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    # If the array is empty, return True
    if len(arr) == 0:
        return True

    # Check if the last element is greater than the first element
    if arr[-1] > arr[0]:
        # If true, we can perform a single right shift operation
        return True

    # If the above condition is not met, iteratively check if the gap
    # between the last and first element can be bridged by cascading right shifts
    gap = abs(arr[-1] - arr[0])
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            gap -= 1
        if gap == 0:
            return True
    return False
```

This script includes a function `move_one_ball` that takes an array as input and returns a boolean value `True` if it's possible to sort the array in non-decreasing order by performing right shift operations, and `False` otherwise. The function first checks if the last element is greater than the first element. If true, it is possible to perform at least one right shift operation. If the array is still not sorted after a single shift, it iteratively checks subsequent elements to see if each element is greater than its previous one. If it finds any such element, it subtracts 1 from the gap between the last and first element, effectively reducing the number of shifts needed. If the gap reaches 0, it is possible to sort the array with right shifts. 

The provided code should be correct and fully self-contained. It can be run as a standalone Python script to test it out.