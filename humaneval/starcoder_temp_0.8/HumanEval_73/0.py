
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
    # Write your code here
    if len(arr) == 1:
        return 0

    arr.sort()
    is_palindrome = lambda x: str(x) == str(x)[::-1]
    n = len(arr)
    count = 0
    for i in range(0, n - 1):
        if not is_palindrome(arr[i] + arr[i + 1]):
            count += 1

    return count
