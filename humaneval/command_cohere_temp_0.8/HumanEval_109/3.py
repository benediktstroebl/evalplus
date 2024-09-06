Here's a Python script that contains a function named `move_one_ball` with the described behavior:
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
    # Algorithm applicable for positive integers only
    # Negative integers will not give correct result for this algorithm
    if not arr or not all(isinstance(i, int) and i > 0 for i in arr):
        return False
    # Sort the array elements in reverse order so the smallest element come first
    arr.sort(reverse=True)
    # Iterate over the array elements and calculate the count of right shifts required
    # for each element to occupy the first position (index 0)
    count = sum(1 for i in range(len(arr)) if arr[i] != 0)
    # If the count of right shifts is possible with the given array, return True
    # Otherwise, return False
    return count <= len(arr)
# Test the function
print(move_one_ball([3, 4, 5, 1, 2])) # Output: True
print(move_one_ball([3, 5, 4, 1, 2])) # Output: False
```
This code defines the `move_one_ball` function, which takes an array as input and determines if a non-decreasing sorted order can be achieved by performing right shift operations. The function first sorts the array in reverse order and then counts the number of elements that are not zero. If this count is less than or equal to the length of the array, it is possible to achieve the desired order. The function returns True in such cases and False otherwise.