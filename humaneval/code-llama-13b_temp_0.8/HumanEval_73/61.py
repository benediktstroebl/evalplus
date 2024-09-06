
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

    # get total number of changes required to make the array palindromic
    total_changes = 0

    # 1) rearrange the array so that all odd numbers appear first, and then all even numbers.
    # 2) make the array palindromic by changing the even numbers at the end so they match the corresponding odd numbers
    # from the beginning.

    # rearrange the array
    rearrange_arr(arr)
    print(arr)

    # find the number of changes required
    total_changes = get_changes(arr)

    return total_changes

