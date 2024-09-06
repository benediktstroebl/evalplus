
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Set up an array of the size of the input array
    # Each element will be the largest index of an element which is not greater
    # than or equal to the element immediately preceding it.
    arr_size = len(arr)
    arr_index = [None] * arr_size

    # Start from the last element. If there is an element to the left which is
    # greater than or equal to this element then the index is the index of the
    # element to the left.
    # If not then the index is the current index.
    # Continue to move back until you reach the first element.
    for index in range(arr_size - 1, -1, -1):
        if index == arr_size - 1:
            arr_index[index] = index
        elif arr[index] <= arr[index + 1]:
            arr_index[index] = arr_index[index + 1]
        else:
            arr_index[index] = index

    # Now that we have the indices, find the first element which is not greater
    # than or equal to the preceding element.
    # Start from the last element and check if the preceding element is greater
    # than or equal to this element. If not then return the current index.
    # If the preceding element is greater then continue to check the next
    # element.
    # If all preceding elements are greater then return -1.
    for index in range(arr_size - 1, -1, -1):
        if index == arr_size - 1:
            return arr_index[index]
        elif arr[arr_index[index]] < arr[index]:
            return arr_index[index]

