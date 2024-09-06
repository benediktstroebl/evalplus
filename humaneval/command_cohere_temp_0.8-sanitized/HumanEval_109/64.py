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
    # Ensure that the input is not empty, this condition serves as a base case
    if len(arr)==0:
        return True
    # Initialize variables
    count=0
    # Use a flag to track the first occurrence of elements in the array while shifting,
    # if an element which has already occurred before remains at the last index,
    # it indicates a successful sorting and we return True
    first_occurrence=dict()
    for i in range(len(arr)):
        first_occurrence[arr[i]]=i
    # Shift the array and track the last index where a element is placed
    for i in range(len(arr)):
        if i==len(arr)-1:
            continue
        while arr[i] in first_occurrence and first_occurrence[arr[i]]>i:
            # If an element which has occurred before is at the current index,
            # this will indicate a successful sorting, hence return True
            if first_occurrence[arr[i]]==i:
                return True
            # Shift the element
            arr[i],arr[len(arr)-1]=arr[len(arr)-1],arr[i]
            # Update the index where the element occurs
            first_occurrence[arr[i]]=-1
            count+=1
        if count>len(arr):
            return False
    return True