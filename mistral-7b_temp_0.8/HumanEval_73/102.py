
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
    # brute force approach, check for all possible palindromes and return the min no. of changes
    # if palindrome is possible using only 1 element, return 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue

            # check for palindrome after swapping the elements
            temp = arr[:]
            temp[i], temp[j] = temp[j], temp[i]
            if is_palindrome(temp):
                return 1

    # if no palindrome is found, return 1 more than the no. of elements in the array
    return len(arr) + 1
