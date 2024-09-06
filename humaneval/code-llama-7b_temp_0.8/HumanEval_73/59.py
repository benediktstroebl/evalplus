
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
    #Verify all elements are in arr are odd
    #Verify all elements in arr are in arr are equal
    #verify arr is a palindrome
    #if arr is a palindrome return 0
    #find first element that is not equal to it's reverse
    #return number of elements between first and last element that are not equal to reverse
    #return 0 if arr is palindromic

    if palindrome(arr):
        return 0

    first = 0
    last = len(arr) - 1
    while arr[first] == arr[last] and first < last:
        first += 1
        last -= 1

    #when first and last are equal, break
    #when first is greater than last, break

    while first < last:
        #keep incrementing first until it's equal to last
        first += 1

        if arr[first] != arr[last]:
            return last - first
