def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Initialize variables for the first and last elements of the array
    first = arr[0]
    last = arr[-1]

    # Iterate over the array to compare elements
    for idx, num in enumerate(arr):
        if idx == 0 and num != first:
            return False
        elif idx == len(arr) - 1 and num != last:
            return False
        elif idx > 0 and num < arr[idx - 1]:
            return False

    # If we reach here, it means the array is sorted in non-decreasing order
    return True