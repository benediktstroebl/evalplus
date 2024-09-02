
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
    #new arr
    new_arr = arr[::-1]
    #compare
    #if same
    if arr == new_arr:
        return 0

    #if diff
    else:
        #create new arr with diff
        diff_arr = [abs(arr[i] - new_arr[i]) for i in range(len(arr))]
        return max(diff_arr)

