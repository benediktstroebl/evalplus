Here's a Python script that includes a self-contained function to solve the problem and handles all the edge cases mentioned in the prompt:
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
    # Base case
    if not arr or len(arr) == 1:
        return True

    # Sort the array and check if the sorted array is equal to the original array
    # with elements shifted one position to the right.
    return move_one_ball(sorted(arr)) == list(arr)[1:][::-1]
```

This function `move_one_ball` recursively sorts the array and then compares it to the original shifted array to determine if it's possible to achieve a non-decreasing order. The base case checks for an empty array or an array with just one element, in which case it returns True.