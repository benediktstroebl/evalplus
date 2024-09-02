
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
    def smallest_change_helper(arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return 1
        first_half = arr[0::2]
        second_half = arr[1::2]
        first_half.append(second_half[0])
        second_half[0] = first_half[-1]
        return 1 + smallest_change_helper(first_half) + smallest_change_helper(second_half)

    return smallest_change_helper(arr
