
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # edge case, k is 0, should return all elements
    # edge case, k is len(arr), should return all elements
    if k == 0:
        return arr
    elif k == len(arr):
        return sorted(arr)[-k:]
    
    # find max
    max_idx = arr.index(max(arr))

    # find first max
    first_max_idx = max_idx

    # find second max
    second_max_idx = max_idx

    # if max idx is 0
    if max_idx == 0:
        first_max_idx = len(arr)-1-k
        second_max_idx = len(arr)-1

    # find first max
    for i in range(0, k):
        if first_max_idx >= len(arr)-1:
            break
        if arr[first_max_idx] < arr[i]:
            first_max_idx = i
    
    # find second max
    for i in range(0, k):
        if second_max_idx >= len(arr)-1:
            break
        if arr[second_max_idx] < arr[i]:
            second_max_idx = i

    return sorted(arr)[first_max_idx:second_max_idx+1]

assert(maximum([-3, -4, 5], 3) == [-4, -3, 5])
assert(maximum([4, -4, 4], 2) == [4, 4])
assert(maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2])
assert(maximum([-1, 2, 1, 2, -1, -2, 1], 3) == [-1, 2, 1])
assert(maximum([], 0) == [])
assert(maximum([1], 1) == [1])
