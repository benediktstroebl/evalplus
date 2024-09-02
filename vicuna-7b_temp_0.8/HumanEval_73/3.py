
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

    # Find the first and last element of the array
    first = arr[0]
    last = arr[-1]

    # Check if the first and last element are the same
    if first == last:
        return 0

    # Check if the array is empty
    if len(arr) == 0:
        return 0

    # Initialize the count of elements to change
    count = 0

    # Loop through the array and check for palindromic subarrays
    for i in range(1, len(arr)):
        # Find the middle element of the subarray
        middle = arr[i]

        # Check if the subarray is a palindrome
        if middle == (first + last) // 2:
            count = len(arr) // 2

            # Check if the subarray can be reduced by one element
            if count > 0 and arr[count] == middle:
                count -= 1

            # Check if the subarray can be reduced by two elements
            if count == 0 and arr[count // 2] == middle:
                count = 1

    return count