
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # brute force -- O(n ^ 2)
    # for idx, elt in enumerate(arr):
    #     if idx == 0:
    #         continue
    #     for previous in arr[:idx]:
    #         if elt <= previous:
    #             return idx
    # return -1

    # sort the array -- O(n log n)
    # sorted_arr = sorted(arr)
    # for idx, elt in enumerate(sorted_arr):
    #     if idx == 0:
    #         continue
    #     if elt <= sorted_arr[idx - 1]:
    #         return idx
    # return -1

    # one-pass -- O(n)
    max_elt = None
    max_elt_idx = -1
    for idx, elt in enumerate(arr):
        if elt > max_elt:
            max_elt = elt
            max_elt_idx = idx
    return max_elt_idx
