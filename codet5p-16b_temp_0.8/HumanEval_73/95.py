
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

    table = {}
    min_diff = 0
    odd = 0
    for i in arr:
        table[i] = False
    
    for i in arr:
        if table[i] == False:
            if i%2 == 0:
                min_diff += i-1
                odd = 1
                table[i] = True
                table[i-1] = True
            else:
                min_diff += i+1
                odd = 1
                table[i] = True
                table[i+1] = True
    return min_diff
