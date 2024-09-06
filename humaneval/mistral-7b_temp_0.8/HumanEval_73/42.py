
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

    arr.sort()
    size = len(arr)
    middle = size // 2

    def isPalindromic(arr):
        return arr[:middle] == arr[::-1][:middle]

    changes = 0
    for i in range(0, size):
        if arr[i] != arr[-i - 1]:
            changes += 1
            if not isPalindromic(arr):
                if arr[i] < arr[-i - 1]:
                    arr[i] = arr[-i - 1]
                else:
                    arr[-i - 1] = arr[i]
    return changes
