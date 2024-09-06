def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables for the first and last elements
    f = arr[0]
    l = arr[-1]
    # Iterate over the array to compare elements
    for i in range(1, len(arr)):
        if arr[i] > f:
            f = arr[i]
        if arr[i] < l:
            l = arr[i]
    # Return False if the array elements are reversed or if the first and last elements are the same
    return f != l and f == l - 1