
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
    forward = reverse = mid = 0
    for i, num in enumerate(arr):
        if i > len(arr) - i - 1:
            break
        if num != arr[i - 1 - forward]:
            if i - forward == len(arr) - 1 - reverse:
                forward += 1
                reverse += 1
                mid = i
            elif i + reverse == len(arr) - 1 - forward:
                forward += 1
            else:
                reverse += 1
    return len(arr) - mid - max(forward, reverse)
