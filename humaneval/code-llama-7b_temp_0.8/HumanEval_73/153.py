
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
    first_half, second_half = list(arr[0::2]), list(arr[1::2])
    first_half.reverse()

    if first_half == second_half:
        return 0

    palindromic_arr = []
    for i in range(len(first_half)):
        palindromic_arr.append(first_half[i])
        palindromic_arr.append(second_half[i])

    return len(arr) - len(palindromic_arr)
