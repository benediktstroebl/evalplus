
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
    # always check for exception
    if arr is None or len(arr) == 0:
        return 0

    # if array is palindrome then no change is required
    if isPalindrome(arr):
        return 0

    # now reverse the array and check for palindrome
    reverseArr = arr.copy()
    reverseArr.reverse()

    # check if reverse array is palindrome
    if isPalindrome(reverseArr):
        return len(arr)

    # if not palindrome then
    # create temp arr and reverse it one time
    tempArr = arr.copy()
    tempArr.reverse()

    # then we compare each element
    # if elements are different then count + 1
    count = 0
    for i in range(0, len(tempArr)):
        if tempArr[i] != arr[i]:
            count += 1

    # return count
    return count

