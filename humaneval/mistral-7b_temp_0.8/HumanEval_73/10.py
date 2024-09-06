
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # Initialize the count of changes to zero.
    count_of_changes = 0

    # Iterate over the array from the middle element to the beginning and the end.
    for i in range(len(arr) // 2):
        # If the elements at the corresponding positions are not equal,
        if arr[i] != arr[len(arr) - 1 - i]:
            # Increment the count of changes.
            count_of_changes += 1
            # Invert the elements at the corresponding positions.
            arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]

    # Return the count of changes.
    return count_of_changes

