
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
    # to hold the final sorted array
    result_arr = []
    
    if arr:
        #to store the rightmost value of the array
        rightmost = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            # to store the leftmost value of the array
            leftmost = arr[0]
            # to check if the rightmost value is greater than the leftmost value
            if rightmost < leftmost:
                return False
            # to check if rightmost value is greater than the element at index i
            elif rightmost > arr[i]:
                # to remove the rightmost value
                arr.remove(rightmost)
                # to append the value at index i as the rightmost value
                arr.append(rightmost)
                # to append the element at index i to the result_arr
                result_arr.append(leftmost)
                # to change the rightmost value to the value at index i
                rightmost = arr[0]
                # to change the leftmost value to the value at index i
                leftmost = arr[i]
        result_arr.append(rightmost)
        return result_arr

    return True
