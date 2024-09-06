import unittest
def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Check if the sorted array can be created by shifting
    return sorted_arr == unique_arr[:len(unique_arr) - 1:-1]