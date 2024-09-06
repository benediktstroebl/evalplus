
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
    # we need to find the position of the maximum element in arr
    # and move that element to position 0
    # and then move the 0th element to the next highest position
    # until we have moved all the elements
    # we can use the index of the maximum element to determine the number of
    # shifts to do
    # for each element in arr
    # 1. keep track of the highest element
    # 2. if the current element is greater than the highest element, replace the
    #    highest element with the current element, update highest element
    # 3. if the current element is less than or equal to the highest element
    #    continue, else do a right shift of the array
    # 4. decrement the number of times the maximum element was encountered
    # 5. if number of times the maximum element was encountered is 0, the array
    #    is sorted
    # 6. return True if the array is sorted, otherwise return False

    # loop through the array to find the maximum element
    # track the position of the maximum element in a variable
    highest_element_position = 0
    highest_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > highest_element:
            highest_element_position = i
            highest_element = arr[i]
    #print(highest_element, highest_element_position)
    # perform the right shift operations until all elements are in non-decreasing
    # order
    # number of times the maximum element was encountered
    times_max_encountered = 0
    while True:
        # find the position of the maximum element
        # loop through the array
        for i in range(1, len(arr)):
            if arr[i] == highest_element:
                times_max_encountered += 1
        # if the maximum element was encountered 'times_max_encountered' times,
        # then the array is sorted
        if times_max_encountered == 0:
            return True
        # otherwise, perform the right shift operations
        # move the maximum element to the first position in the array
        # move the first element to the next
