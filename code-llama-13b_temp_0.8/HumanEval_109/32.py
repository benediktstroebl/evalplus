
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
    # Your code here
    
    # step 1: find the first decreasing element
    # step 2: find the second decreasing element (it cannot be on the left side of the first decreasing element)
    # step 3: if these two elements are not the last two elements, swap them
    # step 4: sort the rest of the array
    # step 5: return True if the result is sorted in ascending order
    
    if len(arr) == 0:
        return True
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            first_decreasing_index = i
            break
    for j in range(first_decreasing_index + 1, len(arr)):
        if arr[j] < arr[first_decreasing_index]:
            second_decreasing_index = j
            break
    # print(arr)
    # print(first_decreasing_index)
    # print(second_decreasing_index)
    if first_decreasing_index == 0 and second_decreasing_index == len(arr) - 1:
        return False
    if second_decreasing_index < len(arr) - 1:
        arr[first_decreasing_index], arr[second_decreasing_index] = arr[second_decreasing_index], arr[first_decreasing_index]
    # print(arr)
    arr[first_decreasing_index + 1:] = sorted(arr[first_decreasing_index + 1:])
    # print(arr)
    for k in range(len(arr) - 1):
        if arr[k] > arr[k + 1]:
            return False
    return True

