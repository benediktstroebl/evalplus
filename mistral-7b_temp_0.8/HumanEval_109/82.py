
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
    arr.sort()

    def helper(arr,n):
        if len(arr) == n:
            return True
        elif len(arr) < n:
            return False
        elif arr[0] < arr[-1]:
            return helper(arr[1:], n)
        else:
            return helper(arr[1:], n)
    return helper(arr,len(arr))
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    #Your code goes here
    #return True if .... else False



    """
    The idea is to check whether we can get a sorted array by doing right
    shift operation. This can be done by checking if the first element is less
    than the last element. If it is true then we can perform right shift
    operation to get a sorted array.
    """
    # return True if arr[0] < arr[-1] else False

    #Time Complexity: O(n)
    #Space Complexity: O(n)
    """
    def move_one_
