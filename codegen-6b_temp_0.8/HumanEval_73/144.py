
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
    if not arr:
        return 0

    arrLen = len(arr)
    # if the array is in one of the special cases that'd make the array a palindromic array, then we return
    if arrLen == 1:
        return 0
    elif arrLen == 2:
        return abs(arr[0] - arr[1])
    elif arr[0] == arr[-1]:
        return 0
    elif arr[0] == arr[-2] and arr[-1] == arr[-3]:
        return 0

    # if the array is larger than 3 elements, we will find the minimum to change to make it a palindrome
    if arrLen > 3:
        minChanges = arrLen
        for i in range(arrLen - 1):
            # we want to find the minumum change that is needed to get the current array value to be the same as the previous
            # value, but only for values that are NOT the beginning or end of the array
            if not (i == arrLen - 1 or i == 0):
                # we start comparing our current value from the front
                for j in range(1, arrLen - 1 - i):
                    # if the current value is the same as the previous value, then we don't need to make any changes
                    # and we skip over the current number
                    if arr[i + j] == arr[i - 1]:
                        continue
                    # otherwise, we want to select the smallest change that will make the value be the same as the previous
                    # value, but with the current number in the value
                    minChanges = min(minChanges, abs(arr[i + j] - arr[i - 1]))
        return minChanges

    # since the array must be 3 elements, we know that it's in one of the special cases, so we return the abs of the
    # difference between the two values
    return abs(arr[0] - arr[1])

