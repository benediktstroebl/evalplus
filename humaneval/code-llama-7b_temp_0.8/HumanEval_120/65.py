
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
    # exceptions
    if not arr or k <= 0 or k > len(arr):
        return []
    
    # traverse the array
    # make sure the current max value is still in the k slots
    # if not, pop the least max value in the k slots
    # put the current max value in the k slots
    k_slots = [-float('inf')] * k
    for num in arr:
        i = 0
        while i < k:
            if k_slots[i] < num:
                break
            i += 1
        if i == k:
            k_slots.pop()
        k_slots.insert(i, num)
    return k_slots

