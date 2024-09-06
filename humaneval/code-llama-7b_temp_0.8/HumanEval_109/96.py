
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
    #  
    # Input Parameters:
    #   arr: Array of integers to be checked for non-decreasing order.
    #
    #   Return:
    #   True if non-decreasing order is possible, otherwise False.
    
    # Base case: The array is empty then it is possible to get non-decreasing
    # order.
    if not arr:
        return True
    # The array has only one element then it is possible to get non-decreasing
    # order.
    if len(arr)==1:
        return True
    # Initialize the current_index, next_index and total number of elements in
    # the array.
    current_index = 0
    next_index = 1
    total_elements = len(arr)
    # Iterate through the array.
    while current_index < total_elements and next_index < total_elements:
        # If the element at the next index is greater than the current element then
        # no non-decreasing order is possible.
        if arr[next_index] > arr[current_index]:
            return False
        # If the next element is greater than the previous element then move the
        # next_index to the next element.
        next_index += 1
        # If the next index is reached and the element is less than the previous
        # element then move the next index to the current index and increase the
        # current index to the next index.
        if next_index == total_elements or arr[next_index] < arr[current_index]:
            next_index = current_index+1
            current_index += 1
    # If the next index is reached and the next_index is greater than the total
    # number of elements then return True.
    if next_index >= total_elements:
        return True
    # Return false otherwise.
    return False
