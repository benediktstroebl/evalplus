
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
    arr.sort()
    
    arr_len = len(arr)
    
    def is_palindrome(x,y):
        return arr[x] == arr[y]
    
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            if is_palindrome(i, j):
                return min(j - i, i + arr_len - j)
    
    return 0

