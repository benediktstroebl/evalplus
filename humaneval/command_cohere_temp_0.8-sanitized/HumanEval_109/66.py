def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Check if the input array is of length 1, 2 or 3.
    # It is possible to sort in non-decreasing order with zero or one shift operation for these cases.
    if len(arr) <= 3:
        return True
    
    # Check if the input array contains a single element or if all elements are equal.
    # In these cases, it is not possible to perform any right shift operations without obtaining a sorted array.
    if len(set(arr)) < len(arr):
        return False
    
    # Check if the input array contains a pair of adjacent elements whose difference is equal to the length of the array.
    # If so, it is possible to sort by right shifting the ball exactly this number of times.
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) == len(arr):
            return True
    
    # If we reach this point, it is not possible to sort the array by right shifting a single ball.
    return False