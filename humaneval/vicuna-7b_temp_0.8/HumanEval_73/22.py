
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
    # Sort the array
    arr = sorted(arr)
    # Initialize a variable to store the minimum number of changes
    min_changes = len(arr)
    # Iterate through the array
    for i in range(1, len(arr)):
        # Check if the first half of the array is the reverse of the second half
        if arr[i:(len(arr) - i)] == arr[:(len(arr) - i)][::-1]:
            # If it is, we've made a change, so update the minimum number of changes
            min_changes -= 1
    return min_changes