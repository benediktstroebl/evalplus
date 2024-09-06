def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables for the first and last elements
    first, last = arr[0], arr[-1]
    # Iterate over the array to compare elements
    for num in arr[1:-1]:
        if num < first:
            first = num
        elif num > last:
            last = num
    # If the array is already sorted in non-decreasing order, return True
    if first <= last:
        return True
    # Otherwise, perform the right shift operation the necessary number of times
    return move_one_ball(arr[1:] + [arr[0]])