
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

    # Input parameter is the list 'arr' of integers 
    if len(arr)==0:
        return True
    # Initialise a variable 'len_arr' to count the number of elements in the list
    len_arr = len(arr)
    # Initialise a variable 'flag' to check if the given list is sorted or not
    flag = False
    # Loop through the array from the last index to first index
    for i in range(len_arr-1,-1,-1):
        # Check if the i th element is greater than the (i-1)th element
        if arr[i]>arr[i-1]:
            # If the i th element is greater than the (i-1)th element, the flag is
            # set to True
            flag = True
            # We create a second array 's' with same elements as the first array
            s = arr
            # Loop through the second array 's'
            for j in range(len_arr):
                # If the (i-1)th element is greater than the (i)th element
                # then we perform a right shift operation on the second array
                if s[j-1]>s[j]:
                    s[j-1], s[j] = s[j], s[j-1]
                # After the right shift operation, if the second array 's'
                # is in non-decreasing order then we can return True
                if s[j]<=s[j-1]:
                    return True
                # If the second array 's' is not in non-decreasing order then
                # we can return False
                if s[j]>s[j-1]:
                    return False

        # If the i th element is less than or equal to the (i-1)th element then
        # the flag is set to False
        else:
            flag = False
    # If the flag is True then we can return True else we can return False
    if flag==True:
        return True
    else:
        return False

