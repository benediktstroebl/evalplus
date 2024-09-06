
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Use linear search to find the largest number
    largest_number = -1
    for i in range(len(arr)):
        if arr[i] > largest_number:
            largest_number = arr[i]
    # Create a new array to store the number of elements that are greater than
    # the element in the new array, using the largest number as a reference.
    number_greater_than_prev = [0] * (largest_number + 1)
    for i in range(len(arr)):
        number_greater_than_prev[arr[i]] += 1
    # Iterate through the original array and use the number of elements greater
    # than the current element to check if the number of elements that are
    # greater than the current element is at least as large as the current
    # element
    for i in range(len(arr)):
        if number_greater_than_prev[arr[i]] >= arr[i]:
            return i
    return -1

