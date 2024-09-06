def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Sort the array and remove duplicates.
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Check if the sorted array can be created by shifting elements to the left.
    for i in range(len(arr)-1):
        if sorted_arr[i] != arr[i+1]:
            return False

    return True