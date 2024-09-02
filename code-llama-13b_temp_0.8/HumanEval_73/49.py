
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
    if len(arr) == 1:
        return 0

    n = len(arr)
    result = 0
    # loop over the array
    for i in range(0, n):
        # loop over the array in reverse
        for j in range(n - 1, -1, -1):
            # if we've found a duplicate, check the rest of the array
            if arr[i] == arr[j]:
                if i == j:
                    # we've found a duplicate at the middle of the array
                    # check the rest of the array
                    if i > 0:
                        result += 1
                        break
                    else:
                        break
                if i > 0:
                    # check the array from the middle of the array to the beginning
                    for k in range(i - 1, -1, -1):
                        # if we've found a duplicate, check the rest of the array
                        if arr[k] == arr[j]:
                            if k == j:
                                result += 1
                                break
                            else:
                                result += 2
                                break
                    break
                else:
                    break
            else:
                result += 1
                break
    return result

