def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique = list(set(arr))
    sorted_arr = sorted(unique)
    # Determine the number of shifts required to sort the array
    max_shift = len(arr) - len(sorted_arr)
    # Check if it's possible to achieve a sorted array through right shifts
    return max_shift >= 0 and move_one_ball(sorted_arr[max_shift:])