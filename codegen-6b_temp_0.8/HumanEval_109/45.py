
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
    # if the array is already sorted, then we return true
    if arr == sorted(arr):
        return True
    # return false if the array is empty
    if len(arr) == 0:
        return True
    # otherwise, we will check if the array is sorted in non-decreasing order by
    # performing the same operation on the given array 3 times
    else:
        for i in range(0, 3):
            # the array is sorted if right shift operation finds the array in a
            # non-decreasing order
            if move_one_ball(arr[1:]) == True:
                return True
        # otherwise when the array is unsorted
        return False

assert(move_one_ball([3, 4, 5, 1, 2])==True)
assert(move_one_ball([3, 5, 4, 1, 2])==False)
assert(move_one_ball([3, 5, 4, 1])==False)
assert(move_one_ball([3, 5, 4])==True)
assert(move_one_ball([3, 1])==True)
assert(move_one_ball([])==True)
assert(move_one_ball([1])==True)
assert(move_one_ball([2, 1])==True)
assert(move_one_ball([8,9, 10, 11, 12, 13])==True)
assert(move_one_ball([1,2,3,4])==False)
assert(move_one_ball([8,11, 10, 12, 13])==True)
assert(move_one_ball([1,2,3,4,5])==False)
assert(move_one_ball([8,11, 10, 12, 13, 5, 4, 3, 2, 1])==True)

