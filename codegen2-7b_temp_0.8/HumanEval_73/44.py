
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
    min_change = float('inf')
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            if is_palindrome(arr[i-1:j+1]):
                change_count = j-i+1
                if change_count < min_change:
                    min_change = change_count
    return min_change if min_change!= float('inf') else 0

