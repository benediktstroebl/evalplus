def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if the last element is the smallest and there is at least one element behind it.
    if arr[-1] >= arr[0] and len(arr) > 1:
        return False

    # If the condition above is not met, we can shift the last element to the first position
    # and get a non-decreasing array.
    return move_one_ball(arr[:-1] + [arr[-1]])