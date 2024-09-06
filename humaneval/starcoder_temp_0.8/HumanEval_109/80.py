
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
    # First we will find the longest subarray with non-increasing elements
    # Longest subarray with non-increasing elements would be at the end of the array
    # So we will move the last element to the start of the array and check whether
    # the subarray sorted or not.
    # We will use 2 pointer approach
    
    # create two pointers, one pointing to the beginning of the array and the other pointing to the end of the array
    # and another pointer to indicate the right shift operation
    start = 0
    end = len(arr) - 1
    shift_count = 0
    
    while(start < end):
        # if the last element is less than the previous element
        # then we have a non-increasing subarray
        if arr[start] > arr[start+1]:
            # shift the end pointer by 1 and increase the shift count by 1
            shift_count += 1
            end -= 1
        # if the last element is greater than the previous element
        # then we don't have a non-increasing subarray
        else:
            # shift the start pointer by 1 and increase the shift count by 1
            shift_count += 1
            start += 1
        # if the shift count is more than or equal to the array length
        # it is not possible to get non-increasing order
        if shift_count >= len(arr):
            return False

    # if the shift count is less than the array length
    # it is possible to get non-increasing order
    return True
