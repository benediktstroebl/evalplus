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
    # Tail Recursion
    # Decreasing result
    # Initialize result as True
    result = True
    # Initialize count as 0
    count = 0
    # Initialize prev as -1
    prev = -1
    # Iterate over array elements
    for idx, num in enumerate(arr):
        # If element is decreasing
        if prev > num:
            # If we have decreasing element
            # And we have not yet performed
            # right shift operation
            if not count:
                # Set count to number of shifts
                count = idx
            # Update prev to current element
            prev = num
        # If we have done right shift
        # operation equal to or more than
        # number of shifts, return False
        elif count and idx >= count:
            result = False
            break
    # If prev is greater than 0,
    # that means there were some
    # decreasing elements at the end
    # of the array
    if prev > 0:
        result = False
    # Return boolean result
    return result