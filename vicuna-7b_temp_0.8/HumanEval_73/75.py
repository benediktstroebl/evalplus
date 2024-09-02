
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
    # Check that the array is not empty
    if not arr:
        return 0

    # Initialize the minimum change to the maximum number of elements
    min_change = len(arr)

    # Check for palindromic cases
    for i in range(1, len(arr)):
        # Start with the middle element
        middle = len(arr) // 2
        # Swap the middle element with any other element
        if arr[middle] != arr[i]:
            min_change = min(min_change, i - middle)

    return min_change