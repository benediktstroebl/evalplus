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
    # Optimization: For a single element array, it is possible to achieve sorted
    # non-decreasing order no matter what the order is.
    if len(arr) == 1:
        return True

    # Optimization: For an empty array, it is possible to achieve a sorted non-
    # decreasing order by performing zero right shift operations.
    if len(arr) == 0:
        return True

    # Creating a boolean list to store whether the 
    # indexth element is greater than the (index-1)th element.
    # If yes, then it is impossible to get sorted array by 
    # performing right shift operations.
    ans = [False] * len(arr)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            ans[i] = True
            break
    # If the above loop exits without any break, it is 
    # possible to achieve a sorted array by performing right 
    # shift operations.
    return not any(ans)