
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Get the index of the first value which is less than the previous value.
    # If there's no such value, return -1.
    def find_first_arr(arr):
        validation = [arr[0]]
        for i in range(1, len(arr)):
            validation.append(arr[i] if arr[i] < validation[-1] else -1)
        return validation[-1]

    # Sort the array so that the smallest value is at the beginning.
    def order_arr(arr):
        arr.sort()

    # Perform the functions above and return the result.
    return find_first_arr(arr)

