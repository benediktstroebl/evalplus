
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Required: compare two numbers, return True if num2 is greater than num1
    # Required: compare two numbers, return True if num2 is less than or equal
    # to num1
    # Required: get the last element of a list
    # Required: get the first element of a list
    # Required: use the equality operator

    if len(arr) <= 1:
        return -1

    last_index = len(arr) - 1

    for index in range(0, last_index):
        if not (arr[index] <= arr[index + 1]) and index == last_index - 1:
            return index
        if not (arr[index] <= arr[index + 1]):
            return index + 1
    return -1

