
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Your code here
    left_index = 0
    right_index = len(arr) - 1
    index = -1
    while left_index <= right_index:
        if arr[left_index] <= arr[left_index + 1]:
            index = left_index
            break
        if arr[right_index] <= arr[right_index - 1]:
            index = right_index
            break
        left_index += 1
        right_index -= 1
    return index

