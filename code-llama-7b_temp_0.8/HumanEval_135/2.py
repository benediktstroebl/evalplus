
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # keys are the values of the array
    # values are the index of the first occurence
    # of a value equal to or greater than it
    positions = {}
    for index in range(len(arr)):
        value = arr[index]
        if value in positions:
            positions[value] = index
        else:
            # if this value is greater than all the previous
            # values then there is no position for it
            if positions and positions[list(positions)[-1]] < index:
                positions[value] = index
    return list(positions.values())[-1] if positions else -1
