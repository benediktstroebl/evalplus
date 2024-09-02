
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

    l = len(arr)
    count_of_odd = 0
    for i in range(l):
        if arr[i] != arr[l - 1 - i]:
            count_of_odd += 1

    # When odd elements are 0, return the number of elements
    # when odd elements are 1, return the number of elements
    return min(count_of_odd - 1, count_of_odd)

