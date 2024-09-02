
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

    # T: O(N^2)
    # S: O(1)
    min_changes = 0
    for i in range(len(arr)):
        if arr[i]!= i + 1:
            min_changes += 1
            m = i
            while arr[m]!= m + 1:
                arr[m], arr[m + 1] = arr[m + 1], arr[m]
                m += 1
                min_changes += 1
    return min_changes

