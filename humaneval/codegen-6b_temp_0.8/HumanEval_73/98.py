
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
    # We can fix the first element, and then move to the second with the smallest change.
    # If we move to the second with the smallest change, we can fix the second element, and so on.
    # If we fix the second element, and then the first with the smallest change, we fix the third and so on.
    # If we fix the third, and then the second, we fix the fourth, and so on.
    # If we fix the fourth, and then the third, we fix the fifth, and so on.
    # If we fix the fifth, and then the fourth, we fix the sixth, and so on.
    # If we fix the sixth, and then the fifth, we fix the seventh, and so on.
    # If we fix the seventh, we can't fix anything more since there will only be 1 possible answer.

    # The first or last element is fixed, and so there is no change to make the array palindromic.
    if arr[0] == arr[-1]:
        return 0

    # We can fix the first element and then move to the second with the smallest change.
    smallest_change = float("inf")
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            smallest_change = 1
            break
    else:
        smallest_change = 0

    return smallest_change + smallest_change_helper(arr[1:])
