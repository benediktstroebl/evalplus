
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
    max_value = -1
    no_shift_index = -1
    shift_start = 0
    shift_end = 0
    for i in range(0, arr_len):
        if arr[i] < max_value:
            no_shift_index = i
        else:
            max_value = arr[i]
    if no_shift_index == -1:
        return True
    for i in range(no_shift_index, arr_len):
        if arr[i] < arr[i - 1]:
            shift_end = i
        else:
            break
    for i in range(0, no_shift_index):
        if arr[i] < arr[i + 1]:
            shift_start = i
        else:
            break
    if shift_end == no_shift_index:
        return move_one_ball(arr[no_shift_index + 1:])
    if shift_start == no_shift_index:
        return move_one_ball(arr[:no_shift_index])
    if shift_start == 0:
        if shift_end == arr_len - 1:
            return True
        if shift_end == arr_len - 2:
            return arr[arr_len - 1] < arr[shift_end + 1]
    return False
