
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Create a list of unique values in the array
    unique_values = set(arr)

    # Loop through the array and check each value
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            # If the element is greater than or equal to the element immediately preceding it, return -1
            return -1
        elif arr[i] in unique_values:
            # If the element is in the set of unique values, return the index of the element
            return i
        else:
            # If the element is not in the set of unique values, add it to the set and continue looping
            unique_values.add(arr[i])

    # If no such element is found, return -1
    return -1