
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
    # end_index: index of the end of the "backward" half
    end_index = len(arr) // 2
    if len(arr) % 2 == 0:
        end_index -= 1

    backward_half = arr[0:end_index+1]
    forward_half = arr[end_index:][::-1]

    changes = 0
    i = 0
    while i < end_index + 1:
        # check if they need to be changed
        if backward_half[i] != forward_half[i]:
            changes += 1
            # if not, update the corresponding index in the forward_half to match the backward_half
            forward_half[forward_half.index(backward_half[i])] = backward_half[i]
        i += 1
    return changes

