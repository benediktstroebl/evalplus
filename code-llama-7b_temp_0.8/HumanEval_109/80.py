
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
    #we will start with a list and have a while loop that will run till the list
    #is empty or it contains 1 element.In each loop, we will find the max number
    #from the list and append it in a new list
    arr_max = []
    while arr:
        max_number = max(arr)
        arr_max.append(max_number)
        arr = arr[0:arr.index(max_number)]+arr[arr.index(max_number)+1:]
    #In the new list if all elements are same then it is possible to make it a 
    #sorted list, if not then it is not possible to make it sorted by performing
    #right shift operations.
    if arr_max == [arr_max[0]]*len(arr_max):
        return True
    else:
        return False



