
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
    
    for i in range(len(arr)):
        # loop over the numbers in the array
        # check if all the numbers in arr are different
        if i > len(arr):
            return False
        # if all the numbers in arr are different, then check if we can sort the array
        elif len(arr) == len(set(arr)):
            # loop over the numbers in the array
            for j in range(len(arr) - 1):
                # loop over the numbers in the array again
                # if the number in the index is bigger than the number in the next index
                if arr[j] > arr[j + 1]:
                    # if the number in the index is bigger than the number in the next index
                    # then move the number in the next index to the number in the index
                    arr[j] = arr[j + 1]
                    # move the number in the index to the number in the next index
                    arr[j + 1] = arr[j]
                # if the number in the index is not bigger than the number in the next index, then continue
                else:
                    continue
            # if the number in the index is not bigger than the number in the next index
            # then the array is sorted and we can return True
            if arr[i] >= arr[i + 1]:
                return True
            # if the number in the index is bigger than the number in the next index
            # then the array is not sorted and we can return False
            else:
                return False
    # if the given array is empty then return True
    return True


