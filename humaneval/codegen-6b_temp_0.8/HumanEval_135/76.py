
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1
    else:
        previous_el = arr[0]
        sub_arr = arr[1:]
        for index, el in enumerate(sub_arr):
            if el >= previous_el:
                previous_el = el
            else:
                if index == len(sub_arr) - 1:
                    return -1
                else:
                    continue
        return index

