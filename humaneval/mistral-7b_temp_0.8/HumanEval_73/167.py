
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
    smallest_change = 0
    middle = len(arr) // 2

    # For each element, we'll be trying to mirror it in the other side
    # of the array. We'll start from the center and work our way out.
    for i in range(middle):
        # Start on the left and work our way to the right.
        # If the right side's element is greater than the left, then we need to flip
        # an element, since the array is not palindromic.
        for j in range(middle - i, len(arr)):
            if arr[j] > arr[i]:
                smallest_change += 1
                break
        # Start on the right and work our way to the left.
        # If the left side's element is greater than the right, then we need to flip
        # an element, since the array is not palindromic.
        for k in range(i + 1, middle):
            if arr[k] > arr[i]:
                smallest_change += 1
                break
    return smallest_change
