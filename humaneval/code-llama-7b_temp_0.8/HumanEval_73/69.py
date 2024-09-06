
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
    # check if list is not palindromic
    if arr[0] != arr[-1]:
        count = 1
        right = arr[-1]
        left = arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i] != right:
                count += 1
                right = arr[i]
            if arr[i] != left:
                count += 1
                left = arr[i]
        return count
    else:
        count = 0
        right = arr[-1]
        left = arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i] != right:
                count += 1
                right = arr[i]
            if arr[i] != left:
                count += 1
                left = arr[i]
        return count

