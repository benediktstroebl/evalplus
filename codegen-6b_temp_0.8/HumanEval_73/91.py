
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
    # The following optimization was found in the comments: `bottom_up` is faster than `top_down` when dealing with large inputs
    bottom_up = [0, 0, 0, 0, 1] + [float('inf')] * (len(arr) - 5)
    top_down = [0, 0, 0, 0, 1] + [float('inf')] * (len(arr) - 5)

    for i in range(1, len(arr) - 1):
        # Go right up to the center
        top_down[i + 1] = 1 + min(top_down[i], top_down[i - 1])
        if i < len(arr) - 2:
            # Go right up to the center, but start going left after 2 elements
            top_down[i + 2] = 1 + min(top_down[i], top_down[i - 2])
        if i < len(arr) - 3:
            # Go right up to the center, but start going left after 3 elements
            top_down[i + 3] = 1 + min(top_down[i], top_down[i - 3])

    for i in range(len(arr) - 3, -1, -1):
        # Go left down to the center
        bottom_up[i - 1] = 1 + min(bottom_up[i], bottom_up[i + 1])
        if i > 1:
            # Go left down to the center, but start going right after 2 elements
            bottom_up[i - 2] = 1 + min(bottom_up[i], bottom_up[i + 2])
        if i > 2:
            # Go left down to the center, but start going right after 3 elements
            bottom_up[i - 3] = 1 + min(bottom_up[i], bottom_up[i + 3])

    return min([top_down[i] + bottom_up[i] for i in range(len(arr))])
