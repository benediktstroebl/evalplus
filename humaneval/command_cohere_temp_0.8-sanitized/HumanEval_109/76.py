def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order
    if len(arr) == 0:
        return True

    # Check if the last element is the smallest and all other elements are greater
    if arr[-1] >= arr[0] and arr[0] <= arr[1]:
        return False

    # If the condition is not met, it is possible to sort by shifting
    return True