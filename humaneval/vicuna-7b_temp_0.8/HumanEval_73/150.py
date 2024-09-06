
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
    # Using two pointers to iterate through the array
    start = 0
    end = len(arr) - 1
    
    # If the current element is the same as the next element, we have a palindrome
    while start < end:
        if arr[start] == arr[end]:
            return 0
        start += 1
        end -= 1

    # If the array is not palindromic, we return the minimum number of elements that need to be changed
    # to make it palindromic
    return 1