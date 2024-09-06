def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if len(arr) == 0:
        return True

    # Use a flag to track if a ball can be moved to the first position to sort the array
    can_move_to_first = False 

    for num in arr:
        # If the current number is smaller than the last number, it can be moved to the first position
        if num < arr[0]:
            can_move_to_first = True
            break

    # If a number smaller than the last number is found, it is possible to sort the array in non-decreasing order
    return can_move_to_first