import sys
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables for the first element and its position
    first_el = arr[0]
    first_pos = 0
    # Iterate over the array to find the position of the first element
    for i in range(1, len(arr)):
        if arr[i] == first_el:
            first_pos = i
            break
    # If the first element is found at a position other than 0, it's possible to sort in non-decreasing order
    if first_pos != 0:
        return True
    # If the first element is not found at any position, it's not possible to sort in non-decreasing order
    return False