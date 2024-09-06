
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
    # Use a queue to sort the array and find the first element in the array
    # because the first element is not considered in the change
    # this is the most efficient way to solve this problem
    n = len(arr)
    q = []
    # sorting the array
    for i in range(n):
        q.append(arr[i])
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    # checking if the array is palindrome
    for i in range(n//2):
        if arr[i] != arr[n-i-1]:
            return n+1
    return n
