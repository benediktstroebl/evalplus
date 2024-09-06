import unittest
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it.
    if not arr:
        return True

    # Check if any element exists in the array that is not in the first half.
    return max(arr) not in arr[:len(arr) // 2]