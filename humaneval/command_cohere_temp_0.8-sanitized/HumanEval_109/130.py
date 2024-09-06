def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Check if the sorted array can be formed by shifting
    return sorted_arr == unique_arr