
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
    # Algorithm:
    # Intuition
    # The solution to the problem is dependent on the relationship between the
    # number of elements in the array and the largest number in the array.

    # If there are more numbers than the largest number, then every number
    # in the array can be greater than or equal to that largest number.

    # If there are the same number of elements and the same number as the largest
    # number, then all numbers are equal.

    # If there are fewer numbers than the largest number, then there must be at
    # least one number that is smaller than all the other numbers.

    # Formally, if there are n numbers in the array, then the largest number is
    # n-1. Thus, if there are fewer numbers than the largest number, then there
    # must be at least one number smaller than the largest number.

    # Algorithm
    # Let's call the largest number in the array 'max' and the number of elements
    # in the array 'n'.

    # If n > max:
    # return True

    # If n == max:
    # return all numbers are equal

    # If n < max:
    # return there is at least one number smaller than all the other numbers.

    # Code
    max_num = arr[-1]
    length = len(arr)
    if length <= max_num:
        return True
    elif length == max_num:
        # check if all the elements are equal
        if len(set(arr)) == 1:
            return True
        else:
            return False
    else:
        return False
