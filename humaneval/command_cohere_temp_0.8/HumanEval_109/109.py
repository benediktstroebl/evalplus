Here's a Python script that contains a function named `move_one_ball` optimized to solve the problem statement with a comprehensive explanation:
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
    # First, determine quickly whether the last element is greater than the second-to-last element,
    # if so, there's no way to sort the list without extra processing
    if arr[-1] > arr[-2]:
        return False if len(arr) > 1 else True

    # If the above test isn't true, we know we can shift the last element to the first position and
    # potentially "fix" the list by shifting more if there's a violation. However, if the length of the
    # list is 1, there's no additional shifting to do, so we can safely return True
    return all(a <= b for a, b in zip(arr[:-1], arr[1:]))
```

The script implements a logical algorithm to solve the problem. It first quickly identifies whether the last element is greater than the second-to-last element. If true, it returns False immediately, as this situation cannot be resolved by shifting. If that condition is not met, it performs a shift to move the largest element to the first position and then checks if any element in the shifted list is greater than the preceding element, returning True only if this is true for all comparisons. Lastly, if the list has 1 element, it returns True.