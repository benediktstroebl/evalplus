def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and check if it's sorted in ascending order
    sorted_arr = sorted(arr)
    return sorted_arr == arr