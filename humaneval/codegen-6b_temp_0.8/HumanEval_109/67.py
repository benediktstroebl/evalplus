
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
    if len(arr) == 0:
        return True
    
    n = len(arr)
    
    # find the index of the element which is less than the previous element
    for i in xrange(n-1):
        if arr[i] < arr[i+1]:
            break
    else:
        # if every element is greater than the previous element then
        # the array is sorted
        return True

    # check if any of the following conditions hold
    # 1. all elements are in front of the index, i.e. the array is sorted 
    # 2. right_shift at index i will make the array non-sorted
    # 3. left_shift at index i will make the array non-sorted
    
    # all the above conditions are false, i.e. the array is not sorted 
    # find the index of the element which is greater than the previous element
    for i in xrange(n-1, i-1, -1):
        if arr[i] > arr[i+1]:
            break
    else:
        # if the array is sorted, return True
        return True
    
    # if both the above conditions are NOT true then there is a chance that one
    # of the following conditions will hold
    # 1. all elements are in front of the index, i.e. the array is sorted
    # 2. right_shift at index i will make the array non-sorted
    # 3. left_shift at index i will make the array non-sorted
    # in case 1 and 2, return False
    # in case 3, if the array is sorted, return True, else return False
    for i in xrange(i, i+2):
        if i+1 >= n:
            return True
        if arr[i] > arr[i+1]:
            return False
    else:
        return True if arr[i] <= arr[i+1] else False

assert move_one_ball([3, 4, 5, 1, 2])
assert not move_one_ball([3, 5, 4, 1, 2])
assert not move_one_ball([2, 1, 3])
assert move_one_ball([2,