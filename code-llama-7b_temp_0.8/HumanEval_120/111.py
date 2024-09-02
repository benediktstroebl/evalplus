
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
    # A: find top k numbers
    if k == 0: return []
    top_k = []
    for i, num in enumerate(arr):
        if i < k:
            top_k.append([num, i])
        else:
            insert_idx = binary_search_idx_for_insert(top_k, num)
            if insert_idx == -1: continue
            if insert_idx == len(top_k):
                top_k[-1][0] = num
            elif num >= top_k[insert_idx][0]:
                top_k[insert_idx][0] = num

    return [num for num, _ in top_k]

