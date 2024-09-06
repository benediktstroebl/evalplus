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
    # Empty array or single element array
    if len(arr)==0 or len(arr)==1:
        return True
        
    # Sort the array
    arr.sort()
    
    # Find the first element's index in the sorted array
    first_el_idx = arr.index(min(arr))
    
    # Find the number of right shifts required to move the first element to 0th position
    num_right_shifts = first_el_idx+1
    
    # Find the number of elements after the first element in the original array
    num_elements_after_first = len(arr)-1-first_el_idx
    
    # Check if num_right_shifts is enough to move the first element to the 0th position
    if num_right_shifts>=num_elements_after_first:
        return True
    else:
        return False