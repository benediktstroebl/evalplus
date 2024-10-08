
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
    def is_palindrome(arr):
        return arr[:] == arr[::-1]

    def get_max_diff(arr):
        max_diff = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if is_palindrome(arr[i:j+1]):
                    max_diff = max(max_diff, j-i)
        return max_diff

    return get_max_diff(arr)

