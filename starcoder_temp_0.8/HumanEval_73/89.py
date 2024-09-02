
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
    # create a set of the arr
    arr_set = set(arr)
    # if we have an odd number of elements we can always add one to make it palindromic
    if len(arr) % 2 == 1:
        return 1
    else:
        # otherwise, loop over the set of elements and see if we can swap any two elements
        count = 0
        for element in arr_set:
            # if we can swap two elements then break
            if (element * 2) in arr_set:
                break
            # otherwise we need to swap
            else:
                count += 1
        return count
