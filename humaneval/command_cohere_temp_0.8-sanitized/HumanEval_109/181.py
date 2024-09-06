def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique = list(set(arr))
    sorted_arr = sorted(unique)

    # Check if the original array can be formed by shifting the sorted array
    return sorted_arr == arr[:len(sorted_arr)]