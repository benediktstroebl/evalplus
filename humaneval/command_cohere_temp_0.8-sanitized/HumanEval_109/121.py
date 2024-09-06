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
    # Calculate the length of the array to determine the maximum number of shifts
    N = len(arr)

    # Check if the len(arr) is larger than 1 to avoid division by zero error
    if N > 1:
        # Calculate the maximum number of right shifts that can be made
        max_shifts = N - 1

        # Initialize count variable to count the number of sorted elements
        count = 0

        # Iterate over the array and check if the current element is greater
        # than the next element in the array
        for i in range(N):
            if arr[i] >= arr[i + 1]:
                count += 1

        # Calculate the required number of right shifts
        required_shifts = count - 1

        # Compare the maximum possible right shifts with the required right shifts
        return required_shifts <= max_shifts

    # If the above operations did not encounter any errors or indexing issues,
    # return True for an empty array or when the above condition is not met
    return True