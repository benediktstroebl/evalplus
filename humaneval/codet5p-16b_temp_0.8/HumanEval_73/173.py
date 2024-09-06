
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
    # b[i] is the number of elements that we need to change to make arr[:i+1] palindrome
    # Time complexity is O(n)
    arr = sorted(arr)
    b = [0]*len(arr)
    b[0] = 1
    for i in range(1, len(arr)):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left)//2
            if arr[mid] - arr[i] < 0:
                right = mid
            else:
                left = mid + 1
        if left > 0:
            b[i] = left - 1
    return min(b) + 1

