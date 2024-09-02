
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

    def check_palindrome(arr):
        palindrome_count = 0
        for i, e in enumerate(arr):
            if i > len(arr) // 2:
                break
            if e != arr[len(arr) - i - 1]:
                palindrome_count += 1
        return palindrome_count

    new_arr = list(arr)
    palindrome_count = check_palindrome(arr)
    return palindrome_count if palindrome_count < 2 else palindrome_count - 1

