
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
    if len(arr) < 1:
        return 0

    count = 0

    # We'll use a sliding window with two pointers, one at the start, and another at the end.
    start = 0
    end = len(arr) - 1

    while start <= end:
        # If the element at the start of the array is different from the element at the end of the array,
        # we'll change the element at the start to the element at the end, and vice versa.
        if arr[start] != arr[end]:
            arr[start] = arr[end]
            arr[end] = arr[start]
            count += 1
        # Otherwise, we move both pointers inwards.
        else:
            start += 1
            end -= 1

    return count
