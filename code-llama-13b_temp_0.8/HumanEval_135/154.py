
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # right = len(arr) - 1
    # left = 0
    # while left < right:
    #     if arr[left] <= arr[left + 1]:
    #         left += 1
    #     elif arr[left] >= arr[right]:
    #         right -= 1
    #     else:
    #         return -1
    # return left

    # O(n) time, O(1) space
    max_seen = arr[0]
    index_to_return = -1
    for idx, val in enumerate(arr):
        if val >= max_seen:
            max_seen = val
        else:
            index_to_return = idx
    return index_to_return
