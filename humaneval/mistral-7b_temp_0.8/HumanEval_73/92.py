
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

    # arr = [1,2,3,5,4,7,9,6]
    # 1 2 3 5 4 7 9 6
    # 0 1 2 1 2 1 0 1

    # 3
    # 2 3 4 3 2 2

    # 0 2 3 2 1 0 1

    # 1
    # 1 2 3 2 1

    # 0 1 2 1 0 1

    # 0 1 1 2 1 0 1

    # 1 2 3 2 1 0 1


    palindrome = []
    palindrome_array = []

    # arr = [1,2,3,5,4,7,9,6]

    for i in range(len(arr)):
        palindrome_array.append(0)

    for i in range(len(arr) - 1, -1, -1
