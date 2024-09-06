
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    largest_index_for_element = {}
    for index, value in enumerate(arr):
        if value in largest_index_for_element:
            largest_index_for_element[value] = index
        else:
            largest_index_for_element[value] = largest_index_for_element.get(value, index)
    return max(
        [
            index
            for index, value in enumerate(arr)
            if index == largest_index_for_element[value]
        ]
    )
