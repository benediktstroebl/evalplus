
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
    
    arr_len = len(arr)
    if arr_len == 0:
        return True
    
    # For all the elements of the array
    for i in range(arr_len-1):
        
        # If the current element is greater than the previous element
        if arr[i] > arr[i+1]:
            
            # Check if the previous element is greater than the current element
            if arr[i-1] > arr[i+1]:
                
                # Move the previous element to the current element in array
                arr[i], arr[i-1] = arr[i-1], arr[i]
                
                # Continue checking all the remaining elements
                for j in range(i+1, arr_len):
                    if arr[j] > arr[i]:
                        arr[j], arr[i] = arr[i], arr[j]
                        
                return True
            
            # If the previous element is not greater than the current element
            else:
                return False
            
    # If none of the above cases is true, no permutation of the array can be
    # achieved
    return False
    
