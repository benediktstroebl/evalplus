def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is equal to the first element of the array.
    first_element = arr[0]
    if any(x == first_element for x in arr[1:]):
        return False

    return True