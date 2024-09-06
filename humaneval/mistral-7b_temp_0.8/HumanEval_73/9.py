
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
    def change_to_palindrome(arr):
        i = 0
        j = len(arr) - 1
        while i < j:
            while i < j and arr[i] < arr[j]:
                i += 1
            while i < j and arr[i] > arr[j]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    arr = change_to_palindrome(arr)
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != i + 1:
            count += 1
    return count


