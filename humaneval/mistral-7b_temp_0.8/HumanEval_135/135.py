
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Creating a list for the unchanged elements
    unchanged = []
    # Creating a list for the changed elements
    changed = []
    # For each element in the given array
    for i in arr:
        # If the element is greater than or equal to the element immediately
        # preceding it, then append it to the list of unchanged elements
        if i >= arr[arr.index(i)-1]:
            unchanged.append(i)
        else:
            # Else append it to the list of changed elements
            changed.append(i)
    # If the list of unchanged elements is empty, then return -1
    if unchanged == []:
        return -1
    # Else, return the index of the last element in the list of changed
    # elements
    else:
        return changed.index(changed[-1])
