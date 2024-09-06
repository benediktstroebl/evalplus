
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
    N = len(arr)
    if N == 0:
        return True

    left_min = arr[0]
    i = 0
    while i < N - 1:
        if arr[i] > left_min:
            smallest_idx = i
            break
        i += 1
    if i == N - 1:
        return True

    # for all other indices
    for j in range(i, N):
        if arr[j] < left_min:
            left_min = arr[j]
            smallest_idx = j

    if smallest_idx == 0:
        # only one option
        return True

    # We know that the smallest index is too small for the left_min
    # and we need to move it to the start of the array
    tmp = arr[smallest_idx]
    arr[smallest_idx] = arr[0]
    arr[0] = tmp


    left_min_arr = arr[:smallest_idx]
    right_min_arr = arr[smallest_idx + 1:]

    left_min_arr.sort()
    right_min_arr.sort()

    if left_min_arr == arr[:smallest_idx] and right_min_arr == arr[smallest_idx + 1:]:
        return True
    else:
        return False


