
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
    # A palindromic array must be symmetric, so the array needs to be split in the middle.
    # In addition, the array needs to be sorted, so that the symmetric array can be seen.
    # Finally, the array is reduced to its palindrome equivalent by finding the median values
    # in each half of the array.
    # The function will return the number of elements that need to be changed in order to make
    # the array symmetric.
    # If the array is already symmetric, the function will return 0.

    # Start by checking if the array is already symmetric. If it is, return 0.
    if arr == arr[::-1]:
        return 0

    # If the array is not symmetric, sort it.
    arr.sort()

    # Split the array into two halves and find the median value for each half.
    mid = len(arr) // 2
    half1 = arr[:mid]
    half2 = arr[mid:]
    median1 = half1[mid]
    median2 = half2[mid]

    # Calculate the number
