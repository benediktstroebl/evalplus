def move_one_ball(arr):
    # if the array is empty, it is possible to sort it in non-decreasing order
    if not arr:
        return True

    # use a counter to keep track of possible shifts
    shifts = 0

    # traverse the array and try to find a neighbor (i.e. a greater element) on the right
    for i in range(len(arr)):
        # if a neighbor is found, check if it can be moved to the current position
        if arr[i] < arr[i+1]:
            shifts += 1

        # if the current element is the largest in the array and a neighbor is not found,
        # it becomes impossible to achieve a non-decreasing order
        if i == len(arr) - 1 and shifts == 0:
            return False

    # return true if any number of shifts is possible
    return True