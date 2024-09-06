Here's a Python script that contains a function named `move_one_ball` encompassing the problem statement above:
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
    # Sort the array and remove duplicate elements
    arr = list(set(arr))
    arr.sort()
    # Verify if the sorted array can be derived by performing right shift operations
    return arr == sorted(arr, reverse=True)
```

This script includes a function `move_one_ball` that takes in a list of numbers as input and returns a boolean indicating whether the list can be sorted in non-decreasing order by performing right shift operations. The function first removes any duplicate elements within the input list and then sorts the list. It checks if the sorted list is equivalent to a list sorted in descending order; if this condition is true, it implies that the original list can be sorted in non-decreasing order by using right shift operations.