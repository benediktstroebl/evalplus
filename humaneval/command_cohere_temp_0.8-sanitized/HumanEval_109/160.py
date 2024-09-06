def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Get the number of right shifts needed to sort the array
    shifts = len(arr) - len(sorted_arr)

    # If it's possible to perform that many shifts, return True
    return shifts >= 0