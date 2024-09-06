Here's a Python script that contains a function named `move_one_ball` inspired by the problem statement provided:
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
    # Implemented Solution
    # Return True if the array is empty or it has only one element.
    if len(arr)==0 or len(arr)==1:
        return True
    # Return False if the array has more than one element and first element
    # is not less than second element.
    if arr[0]>arr[1]:
        return False
    # Iterate over the array to check if array is possible to sort by performing
    # right shift operation.
    for i in range(1,len(arr)):
        # If the current element is greater than the last element, 
        # then return False.
        if arr[i]>=arr[len(arr)-1]:
            return False
    # If all conditions are satisfied, return True.
    return True
```
This `move_one_ball` function will determine whether a given array can be sorted into non-decreasing order through repeated right-shift operations. It returns `True` if it's possible and `False` otherwise. This algorithm first checks if the array has more than one element and if the first element is greater than the second element. If so, it returns `False` as this configuration cannot be sorted. It then iterates over the array, checking each element to see if it is greater than or equal to the last element. If any condition is met, it returns `False`. If not, it returns `True`. 

This solution is O(n), where n is the length of the input array `arr`, as it iterates over the array once, and each element is compared at most once.