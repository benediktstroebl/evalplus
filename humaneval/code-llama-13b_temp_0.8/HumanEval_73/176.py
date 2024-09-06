
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
    if len(arr) == 0:
        return 0
    # first check if the arr is palindromic
    # if palindromic, return 0
    if is_palindrome(arr):
        return 0
    # if not palindromic, begin process
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            # begin process to determine change required
            # first, remove the number that is not in the middle
            temp = arr[len(arr)-i-1]
            arr.remove(temp)
            # second, add that number to the middle
            arr.insert(i, temp)
            # return the count of this change
            return 1

