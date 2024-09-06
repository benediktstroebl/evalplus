
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
    # if the given array is empty then return True
    if len(arr) == 0:
        return True

    # We will iterate through the given array and see if we can find the
    # given array in any order.
    for i in range(len(arr)):
        # initialize a temporary array to store the array after the
        # given array has been sorted
        temp = arr.copy()
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                # if an element in the given array is greater than the
                # array at position 'i', then move all the elements forward
                # one position in the array
                temp.insert(j, temp.pop(i))
                break
        # if after the given array has been sorted, the array is the same as
        # the given array, then a non-decreasing order is achieved
        if arr == temp:
            return True
        # otherwise, a non-decreasing order is not achieved
        else:
            return False

