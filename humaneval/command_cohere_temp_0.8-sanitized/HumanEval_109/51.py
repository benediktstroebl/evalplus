import unittest
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in the first half of the array.
    # If yes, then it is impossible to sort in non-decreasing order.
    return all(ele <= arr[len(arr) // 2] for ele in arr)