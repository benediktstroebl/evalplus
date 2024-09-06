
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
    arr = [str(i) for i in arr]
    print(arr)

    if is_palindrome(arr):
        return 0

    for index in range(len(arr)):
        test_arr = arr.copy()
        for i in range(10):
            test_arr[index] = str(i)
            if is_palindrome(test_arr):
                return 1
    return -1

