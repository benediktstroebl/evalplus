
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr.append(float('inf'))
    last_previous_index = {}
    for index, value in enumerate(arr):
        if value not in last_previous_index:
            last_previous_index[value] = index
        else:
            current_index = index - last_previous_index[value]
            if current_index > last_previous_index[value]:
                last_previous_index[value] = index
    return last_previous_index[min(last_previous_index)]

