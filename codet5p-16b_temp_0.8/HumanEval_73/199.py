
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

    def is_palindromic(array):
        return all(array[i] == array[-(i+1)] for i in range(len(array)//2))
    def all_pals(arr, idx):
        if idx == len(arr):
            return []
        return is_palindromic(arr[idx:]) or all_pals(arr, idx + 1)

    pal_arr = all_pals(arr, 0)
    if not pal_arr:
        return len(arr) - 1
    return len(arr) - len(pal_arr)
