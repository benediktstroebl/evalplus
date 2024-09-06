def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Sort the array and determine its maximum value.
    arr.sort()
    max_val = arr[-1]

    # Iterate through the array and check if there is at least one index i such that arr[i] >= i+1.
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            return True
        if arr[i] == max_val:
            return False

    # If we reach this point, it means that the max element is sorted to the first position and it is not greater than the next element.
    return True