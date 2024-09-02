
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
    # Check if the array is empty
    if len(arr) == 0:
        return True

    # Get the max element in the array
    max_element = max(arr)

    # Initialize the starting index for the shift operation
    start_index = 0

    # Start with the max element in the array
    current_element = max_element

    # Keep track of the current element and the starting index of the current
    # sequence of elements
    current_element_index = [0]
    current_start_index = [start_index]

    # Loop through the array
    for i in range(1, len(arr)):
        # If the current element is less than the previous element, move the
        # current sequence of elements to the front of the array and start a
        # new sequence
        if arr[i] < current_element:
            current_element_index.pop(0)
            current_start_index.pop(0)
            for j in current_start_index:
                arr[j] = arr[j + 1]
            arr.insert(0, arr.pop(current_start_index[-1]))
            current_element = arr[i]
            current_element_index.append(i)
            current_start_index.append(0)
            # If this is the first time the current element is encountered,
            # increment the current sequence length
            if current_element_index[0] == 0:
                current_element_index[0] += 1

        # Otherwise, move the current element to the right position in the array
        else:
            current_start_index[0] += 1

    # If the current element is greater than the previous element, move the
    # current sequence of elements to the front of the array and start a new
    # sequence
    if arr[i] > current_element:
        current_element_index.pop(0)
        current_start_index.pop(0)
        for j in current_start_index:
            arr[j] = arr[j + 1]
        arr.insert(0, arr.pop(current_start_index[-1]))
        current
