
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

    count = 0
    if len(arr) < 2:
        return 0
    for i in range(len(arr)):
        if arr[i]!= i:
            count += 1
            if arr[i] < arr[arr[i]]:
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
            if arr[i]!= arr[len(arr)-i-1]:
                count += 1
                if arr[i] < arr[len(arr)-i-1]:
                    arr[arr[len(arr)-i-1]], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
            if count == len(arr):
                break
    return count

