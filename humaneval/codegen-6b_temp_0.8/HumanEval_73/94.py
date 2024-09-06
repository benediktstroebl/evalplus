
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
    if arr is None:
        return None

    def change_elem(arr_in, index):
        if index >= len(arr_in) - 1:
            return 0
        if arr_in[index] == arr_in[index + 1]:
            arr_in[index] = arr_in[index + 1]
            arr_in[index + 1] = 0
            return 1 + change_elem(arr_in, index + 2)
        else:
            return 0 + change_elem(arr_in, index + 1)

    return change_elem(arr, 0)

