
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

    max_element = max(arr)
    min_element = min(arr)
    middle = arr[len(arr) // 2]
    min_swap = (max_element - middle) + (min_element - middle)

    count = 0
    for i in range(len(arr) // 2):
        if arr[i] == arr[len(arr) - i - 1]:
            continue
        elif arr[i] < arr[len(arr) - i - 1]:
            count += arr[len(arr) - i - 1] - arr[i]
        else:
            count += arr[i] - arr[len(arr) - i - 1]

    if min_swap < count:
        return min_swap
    else:
        return count
