
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
    
    # The required number of shifts to ensure non-decreasing order is:
    # length - num of elements moves to the left                                
    #           *(length - num of elements) = moves to the right
    #         sum of all moves to the right - sum of all moves to the left
    #         *sum_of_all_moves_to_left = moves to the right
    #    # Here the difference between the two sides:
    #    * the number of moves to the right > moves to the left
    #    # sum of moves to the right > sum of moves to the left
    if (len(arr) - sum(arr)) % 2 == 0:
        return True
    else:
        return False
    