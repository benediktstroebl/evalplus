Here's a Python script that contains a function named `move_one_ball` that solves the problem you've described:
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
    # Determine if the array is empty or not.
    if len(arr) == 0:
        return True
    # Initialize variables that are used to determine the possibilities of moving elements.
    b_pos = 0
    a_pos = len(arr) - 1
    while a_pos - b_pos > 1:
        if arr[b_pos] >= arr[a_pos]:
            a_pos -= 1
        else:
            b_pos += 1
    # If the two pointers meet, it is not possible to sort the array. Otherwise, it is possible.
    return a_pos != len(arr) - 1
```

This script includes a function named `move_one_ball` that takes an array as input and returns either `True` or `False` depending on whether the specified operation can sort the array in non-decreasing order or not. You can use this function according to the problem you described. 

The provided code is deterministic and will work for arrays with unique elements. Let's say the length of the array is `n`, the time complexity of this solution is O(n).