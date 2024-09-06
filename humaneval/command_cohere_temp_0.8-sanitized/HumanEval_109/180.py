def move_one_ball(arr):
    # Base case: If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Sort the array in place using the list method 'sorted'.
    # This will arrange the elements in ascending order.
    arr.sort()
    
    # Verify if the sorted array is in non-decreasing order.
    # If the array contains a decreasing element, it's not valid.
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True