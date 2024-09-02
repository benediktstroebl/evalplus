
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
    array = arr[:]

    def reverse_slice(a, b):
        r = a + b - 1
        while a < b:
            array[a], array[r] = array[r], array[a]
            a += 1
            r -= 1

    def palindrome_slice(a, b):
        r = a + b - 1
        while a < b:
            if array[a] != array[r]:
                return False
            a += 1
            r -= 1
        return True

    l = 0
    r = len(array) - 1

    while l < r:
        if palindrome_slice(l, r):
            return 0
        reverse_slice(l, r)
        l += 1
        r -= 1

    return l
