
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
    #base case
    if l <= 1: return 0

    #forward pass
    #make two palindromes
    arr_rev = arr[::-1]
    # i: start index, j: end index
    i = 0
    j = l - 1

    forward_min = float("inf")
    while i <= j:
        #forward_min = min(forward_min, arr[i], arr_rev[j])
        forward_min = min(forward_min, arr[i], arr_rev[j])
        #increase i by 1 and decrease j by 1
        i += 1
        j -= 1

    #backward pass
    backward_min = float("inf")
    i = 0
    j = l - 1

    while i <= j:
        #backward_min = min(backward_min, arr[i], arr_rev[j])
        backward_min = min(backward_min, arr[i], arr_rev[j])
        #increase i by 1 and decrease j by 1
        i += 1
        j -= 1

    #forward_min = min(forward_min, arr[i], arr_rev[j])
    #backward_min = min(backward_min, arr[i], arr_rev[j])
    #return min(forward_min, backward_min)
    return min(forward_min, backward_min)




