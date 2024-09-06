
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

    sum_of_differences = 0
    for i in range(len(arr)):
        # check if the number is greater than the number on the other end of the array
        if arr[i] > arr[len(arr)-1-i]:
            # subtract the difference of the numbers
            sum_of_differences += arr[i] - arr[len(arr)-1-i]
            arr[i] = arr[len(arr)-1-i]
    return sum_of_differences
