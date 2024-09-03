def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is determine if
    it is possible to get an array sorted in 
    non-decreasing order by performing the following operation on the given array:
    You are allowed to perform right shift operation any number of times.
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 
    
    One can is done, the last element will be shifted to the first position. This means we can
    done by performing a right shift
    operation on each element of the array. 
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. the first index. 
    This done done done. the task of possibleone: possible to get non-decreasing order by performing
    the above operation on the given array? 
    
    One right shift operation can be performed on each element in the array.
    """
    return sum([x[i-1] > x for i,x in enumerate(arr)]) == 0