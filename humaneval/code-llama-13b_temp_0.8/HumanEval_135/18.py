
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Sort arr
    arr.sort()
    # Make a copy of arr
    arr2 = arr.copy()
    # Initialize a pointer at 0
    pointer = 0
    # Go through arr2
    for i in range(len(arr2)):
        # If arr[i] is less than arr[i - 1], increment pointer
        if arr2[i] < arr2[i - 1]:
            pointer += 1
            # Swap the elements to make it ascending order
            arr2[i], arr2[pointer] = arr2[pointer], arr2[i]
        # If not, return pointer - 1
        else:
            return pointer - 1
    # Return -1 if pointer is len(arr2) - 1
    if pointer == len(arr2) - 1:
        return -1
