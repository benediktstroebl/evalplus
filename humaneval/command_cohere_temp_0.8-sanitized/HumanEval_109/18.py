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

    Optimization:
    The 2D array approach takes O(N^2) time and O(N) auxiliary space. 
    A better method is to maintain an auxiliary array 'ans' with same size as of 
    array 'arr'. The auxiliary array 'ans' initialized with True for all positions.
    Now we iterate the main array 'arr' and do the following
        1. If the current element is smaller than the last element of 
          auxiliary array 'ans' assignment is performed(set the ith position 
          of 'ans' to False).
        2. If the current element is greater than the last element of 
          auxiliary array 'ans' we return False.
    The time complexity is now O(N) and auxiliary space is O(N).
    """

    # Initialize an array of the same size as arr with True values
    ans = [True for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > arr[i-1]:
            return False
        if arr[i] < arr[i-1] and not ans[i-1]:
            ans[i-1] = False
    return True