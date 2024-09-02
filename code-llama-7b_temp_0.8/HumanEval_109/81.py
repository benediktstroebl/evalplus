
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
    # Initialize the index as 0
    index = 0
    # Initialize the boolean variable 'flag' as False
    flag = False
    # Make a copy of the array to not make any modifications to the original array
    arr_copy = arr.copy()
    # The outer loop will run till the given array length
    while index < len(arr):
        # If the array is already in non-decreasing order then return True
        if arr_copy == sorted(arr_copy):
            return True
        # To check if the given array can be converted to non-decreasing order
        # by performing the right shift operation on the array, the value of index
        # must be greater than or equal to the minimum value of the array
        if arr_copy[index] >= arr_copy[index + 1]:
            # Initialize the boolean variable 'flag' as True
            flag = True
            # Break the inner while loop
            break
        # Increment the index by 1
        index += 1
    # If the array is in non-decreasing order then return True
    if arr_copy == sorted(arr_copy):
        return True
    # If 'flag' is True then the given array can be converted to non-decreasing
    # order by performing the right shift operation on the array
    if flag:
        # The inner while loop will run till the index value is greater than the
        # length of the given array
        while index <= len(arr):
            # Increment the index by 1
            index += 1
            # Perform the right shift operation on the array
            arr_copy.append(arr_copy[0])
            arr_copy.pop(0)
            # If the array is in non-decreasing order then return True
            if arr_copy == sorted(arr_copy):
                return True
        # Return False
        return False
    # If 'flag' is False then the given array can not be converted to non-decreasing
    # order by performing the right shift operation on the array
    return False

