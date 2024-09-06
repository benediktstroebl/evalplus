Here's a Python script that contains a function named `move_one_ball` with the described behavior, followed by a set of tests to validate its correctness:
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
    # Base case: An empty array is considered valid
    if len(arr) == 0:
        return True

    # Check if the array can be sorted by shifting right
    # Ensure the first element is the smallest, then shift until it's in the right place
    first_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < first_element:
            first_element = arr[i]
            arr[0] = first_element
            del arr[i]

    return move_one_ball(arr)

# Test Suite
def test_move_one_ball():
    assert move_one_ball([3, 4, 5, 1, 2]) == True
    assert move_one_ball([3, 5, 4, 1, 2]) == False
    assert move_one_ball([1]) == True
    assert move_one_ball([1, 1]) == False
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([5, 4, 3, 2, 1]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert move_one_ball([]) == True

test_move_one_ball()
```

In the provided code, a recursive approach is used, where the function first checks if the array has one element or is empty, in which case it returns True. If there's more than one element, the first element is deemed as the smallest and is moved to the front. The function then recursively checks if the remaining array can be sorted. 

The test suite contains a series of tests with different inputs to validate the correctness of the `move_one_ball` function and ensure it aligns with the expected behavior outlined in the problem statement.