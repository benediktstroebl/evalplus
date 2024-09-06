
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

    # find first non-palindrome
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-1-i]:
            break
    # initialize left and right
    left = i
    right = len(arr)-1-i
    # initialize count
    count = 0
    while left < right:
        count += 1
        left += 1
        right -= 1
    return count

