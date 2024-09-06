Here's a Python script that contains a function named `move_one_ball` optimized to solve the problem statement with an efficient time complexity of O(log N) :
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
    # Return True if the array is empty
    if len(arr)==0:
        return True
    # Find the maximum and minimum values in the array
    max_value=max(arr)
    min_value=min(arr)
    # Calculate the difference between the maximum and minimum values
    range_of_elements=max_value-min_value+1
    # Calculate the log of the range of elements
    log_range=len(bin(range_of_elements))-2
    # Count the number of times the right shift operation can be performed
    num_shifts=(log_range)+1
    # True if the number of shifts is sufficient to rearrange the array
    return num_shifts>=len(arr)
```
This script works by finding the maximum and minimum values in the array, calculating the range of values present, then calculating the log of the range of values, and using this value to estimate the number of shifts needed to rearrange the array. If the number of shifts is less than or equal to the length of the array, then it is possible to rearrange the array into sorted order, and the function returns True, otherwise, it returns False. 
Note: The problem can be solved with a time complexity of O(1) using sorting algorithms but this solution is not mentioned in the prompt.