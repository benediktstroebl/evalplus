
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr:
        return -1

    # Create a hashmap with the value of the previous element in a tuple ('current', previous_element)
    # if the current element is greater than or equal to the last element in the array then
    # the value 'current' is greater than the 'previous_element'
    max_arr = {}
    for i, v in enumerate(arr):
        if not max_arr:
            max_arr[(i-1, v)] = i
        elif max_arr[(i-1, v)] < i:
            max_arr[(i-1, v)] = i
        else:
            continue

    return max(max_arr.keys(), key=lambda x: x[1])[0]

