
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
        # If we only have one element, there is no change
        return 0

    max_diff = 0
    for i in range(len(arr)):
        j = len(arr) - 1 - i
        if i < j:
            if arr[i] > arr[j]:
                # If we have a number that is greater than the previous number, then we are handing over
                # to the next element
                max_diff += 1
        else:
            if arr[i] < arr[j]:
                # If we have a number that is less than the previous number, then we are handing over
                # to the previous element
                max_diff += 1

    return max_diff

