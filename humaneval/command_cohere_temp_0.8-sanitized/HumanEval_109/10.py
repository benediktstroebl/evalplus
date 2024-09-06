def move_one_ball(arr):
    # Base case: If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Sort the array in place using the list method 'sorted'.
    # This will arrange the elements in non-decreasing order.
    arr.sort()
    
    # Check if the sorted array is equal to the original array.
    # If they are equal, it means a single ball shift would achieve the sorting.
    return arr == sorted(arr)