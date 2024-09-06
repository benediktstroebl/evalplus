
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
    def find_max_k_elements(k, arr):
        """
        Given a non-empty array, find the max k elements in it.
        """
        start = 0
        end = len(arr) - k
        res = []
        while start < end:
            res.append(arr[start])
            start += 1
        return res

    if not arr or k <= 0:
        return []
    max_k_elements = find_max_k_elements(k, arr)
    max_num = max_k_elements[-1]
    # binary search
    start = 0
    end = len(max_k_elements) - 1
    while start < end:
        mid = (start + end)/2
        if max_k_elements[mid] < max_num:
            start = mid + 1
        else:
            end = mid
    return max_k_elements[:start+1]

