
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
    # Your code here
    def is_palindrome(arr):
        for i in range(len(arr)):
            if arr[i] != arr[len(arr)-i-1]:
                return False
        return True

    l = []
    while not is_palindrome(arr):
        if len(arr) == 1:
            return 1
        for i in range(len(arr)-1):
            if arr[i] == arr[len(arr)-1-i]:
                continue
            else:
                arr[len(arr)-1-i], arr[i] = arr[i], arr[len(arr)-1-i]
                l.append(arr[i])
                break

    return len(l)

