
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
    # Code Here
    
    n = len(arr)
    
    # Corner Case:
    if(n==0):
        return True
        
    # To store the index where the element is greater than the previous element.
    lst = []
    for i in range(1,n):
        if(arr[i]<=arr[i-1]):
            lst.append(i)
            
    # If no such index exists, then the array is already sorted in non-decreasing order.
    if(len(lst)==0):
        return True
    
    # Corner case to check if the last element is less than the first element.
    if(arr[0]<=arr[n-1]):
        return False
    
    # To check if it is possible to get the sorted array by performing right shift operation
    # at all the indices stored in the list 'lst'
    for i in lst:
        if(arr[i-1]>arr[i+1]):
            return False
    return True

