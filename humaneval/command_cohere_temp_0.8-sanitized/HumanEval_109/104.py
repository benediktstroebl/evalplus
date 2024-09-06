def move_one_ball(arr):
    # if the array is empty, it is always possible to sort it
    if not arr:
        return True

    # use a counter to keep track of possible shifts
    shifts = 0

    # traverse the array and try to find a adjacent larger element
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            shifts += 1
            if shifts == len(arr) - 1:
                return True

    return False