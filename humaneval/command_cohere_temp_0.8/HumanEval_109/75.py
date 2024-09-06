Here's a Python script that contains a function named `move_one_ball` pertaining to the problem statement:
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
    # Define an array of variables `count` counting the occurrences of every
    # element in the input array. This is done so that we can determine if the
    # input array can be sorted in non-decreasing order after performing right
    # shift operations.
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1

    # Define an array of variables `right_shifts` that will count the number of
    # right shifts required to sort every element (in order of appearance) to
    # its correct position.
    right_shifts = [0] * (max(arr) + 1)
    for i in range(1, len(arr)):
        right_shifts[arr[i]] += 1

    # Initialize the variable `max_right_shifts` to store the maximum number of
    # right shifts required to sort the input array in non-decreasing order.
    max_right_shifts = max(right_shifts)

    # If the array is empty, it is trivially sorted so return True.
    if not arr:
        return True

    # If the input array is a single element, it is already sorted so return
    # True.
    if len(arr) == 1:
        return True

    # If there is more than one element in the array, then the maximum number
    # of right shifts must be 0 (since the largest element must be in its
    # correct position and thus not need to be shifted).
    return max_right_shifts == 0
```

This script will determine whether a given array can be sorted through repeated right shifts into a non-decreasing order. It returns `True` if possible, and `False` otherwise. This is achieved by first counting the occurrences of every element in the input array to arrange them in a count array `count`. Subsequently, a `right_shifts` array is created to count the number of right shifts required to sort every element to its correct position. The script then determines the maximum number of right shifts required to sort the input array and returns `True` if this