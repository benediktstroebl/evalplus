
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

    # Sort the array
    arr.sort()

    # Create a dictionary
    dict = {}
    dict[arr[0]] = 0

    # Traverse the array
    for index in range(1, len(arr)):
        if arr[index] > dict[arr[index - 1]]:
            dict[arr[index]] = arr[index - 1]
        else:
            dict[arr[index]] = arr[index]

    # Traverse the array again and get the last value
    for value in reversed(arr):
        if value >= dict[value]:
            return arr.index(value)

    return -1
