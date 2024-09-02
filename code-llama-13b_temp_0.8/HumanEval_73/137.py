
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
    if len(arr) < 2:
        return 0

    change_count = 0
    i = 0
    j = len(arr) - 1

    # Get the left most non-equal element
    while arr[i] == arr[j]:
        if i >= j:
            return 0
        i += 1
        j -= 1

    # If the element in the left is less than the one on the right,
    # we need to remove the left element and add the right element
    if arr[i] < arr[j]:
        change_count += j - i
        return change_count

    # If the element in the left is greater than the one on the right,
    # we need to remove the right element and add the left element
    change_count += get_deletion_count(arr, i + 1, j)
    change_count += get_insertion_count(arr, i, j - 1)
    return change_count

