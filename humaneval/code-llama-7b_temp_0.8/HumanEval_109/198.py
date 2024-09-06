
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
    #get the length of the array
    n=len(arr)
    #if the array is empty, return true
    if n==0:
        return True
    
    #if the array is not empty and contains more than one element, 
    #loop through the array and check if the array can be sorted by performing
    #right shift operations
    for i in range(n-1):
        #if any element is smaller than the previous element, return false
        if arr[i]>arr[i+1]:
            return False
    #return true if the array is already sorted
    if arr==sorted(arr):
        return True
    #perform right shift operations
    for i in range(n-1):
        #if the element is greater than the previous element, perform right shift
        #operation
        if arr[i]>arr[i+1]:
            #perform right shift operation
            arr[i+1:] = arr[i:-1]
            arr[0]=arr[-1]
            #if the array is already sorted, return true
            if arr==sorted(arr):
                return True
    #if the array cannot be sorted even after performing all possible right shift
    #operations, return false
    return False

