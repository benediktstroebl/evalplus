
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

    if len(arr) == 0 or len(arr) == 1:
        return True

    def _move_one_ball(arr, start_idx):
        """Helper function to recursively check if there is a way to move one
        ball in an array starting at'start_idx' in the given array.

        Returns:
            True if we can move one ball in an array by performing right shift
            operation in the given array, else return False.

        """
        # Base Case: if start_idx is the last index of the array
        if start_idx == len(arr) - 1:
            return True

        # If we can move one ball in a sub-array starting at'start_idx', then we
        # should be able to move one ball in the given array as well.
        if _move_one_ball(arr, start_idx + 1):
            return True

        # If we are at the last index of the given array and the previous check
        # didn't work out, then we shouldn't be able to move one ball in the
        # given array.
        if start_idx == len(arr) - 2:
            return False

        # Check if we can move one ball starting at'start_idx' by performing
        # right shift operation.
        next_idx = start_idx + 2
        while next_idx < len(arr) and arr[next_idx] >= arr[next_idx - 1]:
            next_idx += 1

        # If we are at the last index of the array and the next_idx is not the
        # last index of the array, then we cannot move one ball in the given
        # array by performing right shift operation starting at'start_idx'
        if next_idx == len(arr):
            return False

        # If we are at the last index of the array and the next_idx is the last
        # index of the array, then we can move one ball in the given array by
        # performing right shift operation starting at'start_idx'
        if next_idx == len(arr) - 1:
            return True

        # In any other case, we should be able to move one ball in the given
        # array by performing right shift operation starting at'start_idx'
        return _move_one_ball(arr, next_idx)

    return _move_one_
