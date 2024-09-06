def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    sorted_arr = sorted(set(arr))
    unique_count = len(sorted_arr)

    # Calculate the required number of shifts
    total_shifts = unique_count - 1

    # Check if it's possible to achieve sorted order after shifting
    return total_shifts >= 0 and total_shifts % unique_count == 0