
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
    # check for empty array
    if arr==[]:
        return True
    
    # find the minimum element in the array
    min_index=arr.index(min(arr))
    # find the maximum element in the array
    max_index=arr.index(max(arr))
    
    # if minimum element is in the first half of the array
    if min_index<max_index:
        return True
    
    # return False if maximum element is not at the end
    if max_index!=len(arr)-1:
        return False
    
    # find the total number of right shifts required to make the array sorted
    shift_count=0
    for i in range(max_index):
        if arr[i]>arr[i+1]:
            shift_count+=1
    # return True if total shifts are even
    if shift_count%2==0:
        return True
    return False
