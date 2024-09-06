
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
    if len(arr) == 1:
        return True

    # to_move and moved are used to keep track of unsorted and sorted
    # elements
    to_move = [i for i, val in enumerate(arr) if val == min(arr)]
    moved = []
    while to_move:
        elem = to_move.pop()
        if elem == arr[-1]:
            # If arr[-1] is in to_move it means there is only one element in
            # to_move and arr[-1] is the last element of the arr
            return True
        if elem == moved[-1]:
            continue
        elif elem < moved[-1]:
            return False
        else:
            moved.append(elem)
            to_move.extend([i for i, val in enumerate(arr) if val == elem])
    return True

