def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Find the largest index i such that arr[i] <= sorted_arr[0]
    # This index will be the pivot point where the rightmost ball will end up
    i = 0
    for j in range(len(arr)):
        if arr[j] <= sorted_arr[0]:
            i = j
            break

    # If the first element of sorted_arr is larger than all elements in arr,
    # it's not possible to achieve a non-decreasing order
    if i == len(arr):
        return False

    # Shift the ball from index i to the first position
    arr[0], arr[i] = arr[i], arr[0]
    del arr[i]

    # Now, check if the remaining balls (except the first one) are sorted
    return move_one_ball(arr[1:]) and sorted_arr[1:] == arr[1:]