
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
    first_l = 2 if l % 2 == 0 else 1
    if l < first_l:
        #we can't handle l < first_l
        return -1

    #let's define one-then-one as a palindrome
    #ie. 1, 2, 3, 2, 1
    one_then_one = -1 * l + 1
    count = 0
    for i in range(first_l // 2):
        if arr[i] != arr[l - 1 - i]:
            count += 1
    if count < one_then_one:
        return count
    else:
        return one_then_one

