def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    # Initialize variables for the first and last elements
    f_el = arr[0]
    l_el = arr[-1]
    # Iterate over the array to compare elements
    for el in arr[1:-1]:
        if el > f_el:
            f_el = el
        elif el < l_el:
            l_el = el
    # Check if the first element can be in the correct position
    if f_el <= l_el:
        return True
    # Check if the last element can be in the correct position
    if l_el <= f_el:
        return True
    # If neither element can be in the correct position, return False
    return False