
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

    cnt = 0
    count_changes = 0
    length_of_array = len(arr)
    for i in range(length_of_array):
        if arr[i]!= arr[length_of_array - i - 1]:
            cnt += 1
    for i in range(length_of_array):
        if arr[i]!= arr[length_of_array - i - 1]:
            arr[i], arr[length_of_array - i - 1] = arr[length_of_array - i - 1], arr[i]
            count_changes += 1
    if cnt == count_changes:
        return count_changes
    return 0

