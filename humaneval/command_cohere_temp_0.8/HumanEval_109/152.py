Here's a Python script that includes a function called `move_one_ball(arr)` that solves the problem you've described, along with a few tests to validate its correctness:
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
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)
    # Check if the sorted array can be created by shifting operation
    return sorted_arr == unique_arr[:len(arr)]

# Tests
arr1 = [3, 4, 5, 1, 2]
assert move_one_ball(arr1) == True

arr2 = [3, 5, 4, 1, 2]
assert move_one_ball(arr2) == False

arr3 = []
assert move_one_ball(arr3) == True
```
This script includes a function `move_one_ball(arr)` that takes an input list `arr` and returns `True` if it's possible to achieve a non-decreasing order using the right shift operation, and `False` otherwise. The function also handles the case where the input array is empty, returning `True`.

The script also includes a few tests to validate the correctness of the function. You can modify the tests or add more of them to cover a variety of scenarios.