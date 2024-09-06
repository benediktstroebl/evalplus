
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Get the largest value in the array
    max_value = max(arr)
    # Count the number of occurrences of each value
    count = [0] * (max_value + 1)
    for value in arr:
        count[value] += 1
    # Figure out the position in the count array of the first
    # value which is greater than or equal to it.
    current_pos = 0
    for value in arr:
        if value <= current_pos:
            count[current_pos] -= 1
            current_pos += 1
        else:
            break
    # If current_pos is at the end of the array, then all values
    # in the array are less than or equal to it.
    if current_pos == len(arr):
        return -1
    else:
        return current_pos - 1
