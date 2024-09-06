
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

    # If list is empty return true
    if len(arr) == 0:
        return True

    # If arr[0] > arr[1], return false
    if arr[0] > arr[1]:
        return False

    # Mark the number of times the number is swapped in the array
    swapped = 0

    # Run a loop to compare adjacent elements
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            # If the number is swapped, increment swapped count by 1
            swapped += 1

            # Swap the number with the previous one
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

            # If any number is swapped, repeat the loop to compare adjacent elements
            # If the number of times the number is swapped is equal to the number of
            # elements in the list, the given array can't be made non-decreasing by
            # performing right shift operations
            if swapped == len(arr):
                return False

    # If the array elements are not swapped, the list can be made non-decreasing by
    # performing the right shift operations
    return True
