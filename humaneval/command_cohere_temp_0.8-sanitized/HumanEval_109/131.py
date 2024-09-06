def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is equal to the first element of the array.
    # If so, it is possible to sort by right shifting.
    if arr[0] == arr[1]:
        return True

    # Check if the first and last element are equal, and also if the second last element is equal to the first element.
    # This is to account for the possibility that the first and last element are the same, and the second last element is the same as the first element.
    if arr[0] == arr[-1] and arr[0] == arr[-2]:
        return True

    # If the first and last element are equal, but the second last element is not equal to the first element,
    # then it is not possible to sort the array in non-decreasing order.
    if arr[0] == arr[-1] and arr[0] != arr[-2]:
        return False

    # If the first element is not equal to the last element, then it is possible to sort the array in non-decreasing order.
    return True