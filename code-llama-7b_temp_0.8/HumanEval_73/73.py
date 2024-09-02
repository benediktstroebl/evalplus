
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
    i, j = 0, len(arr)-1
    count = 0

    while i < j:
        # If the i and j elements are the same we can move to next iteration
        if arr[i] == arr[j]:
            i += 1
            j -= 1
            continue

        # If arr[i] and arr[j] are not the same, we need to move to the next iteration
        if arr[i] == arr[j-1]:
            j -= 1
            continue

        if arr[i] == arr[j+1]:
            i += 1
            continue

        # If arr[i] and arr[j] are not the same and arr[i] is not equal to arr[j-1] and arr[i] is not equal to arr[j+1]
        # we need to increment the count and move to the next iteration
        count += 1
        i += 1
        j -= 1

    return count

