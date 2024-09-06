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
    # Empty array, any number of shifts will work!
    if len(arr) == 0:
        return True

    # Use a counter to keep track of distinct elements
    count = len(arr)

    # Loop to determine if any duplicate elements exist
    for i in range(len(arr)):
        # Count decreases if same element is encountered
        count -= (arr[i] == arr[i-1])

    # If count is 0, means all elements are distinct
    # and it is possible to sort using right shifts
    return count == 0
```

The function works as follows:
1. It first checks if the array is empty, and since any number of shifts would work for an empty array, it returns True in this case.
2. It then uses a counter to keep track of how many distinct elements are in the array. This is done by comparing each element to its previous one and decrementing the count if they are the same.
3. If the count eventually becomes 0, that means all elements are distinct, and it would be possible to sort the array in non-decreasing order using right shifts. The function returns True in this case.
4. If there's at least one duplicate element, the count will not reach 0, and the function returns False. 

This algorithm has a time complexity of `O(n)` where `n` is the length of the input array `arr`. It uses a single variable `count` to keep track of the distinct elements, performing a constant-time operation for each element in the array.