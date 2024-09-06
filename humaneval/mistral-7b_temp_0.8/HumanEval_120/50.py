
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
    if not arr:
        return []
    max_k = max(arr)
    max_heap = []
    for num in arr:
        if max_heap and max_heap[0] < num:
            max_heap = [num] + max_heap
        elif len(max_heap) < k:
            max_heap.append(num)
        else:
            if num > max_heap[0]:
                max_heap[0] = num
    return max_heap[0:k]
