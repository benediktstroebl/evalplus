
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
    """
    input: [-3, -4, 5], k = 3
    output: [-4, -3, 5]
    
    input: [4, -4, 4], k = 2
    output: [4, 4]
    
    input: [-3, 2, 1, 2, -1, -2, 1], k = 1
    output: [2]
    """
    if k == 0:
        return []

    if k == 1:
        return list(sorted(arr, reverse=True))

    if len(arr) == 1:
        return arr

    f = arr[0]
    s = [f]

    for n in arr[1:]:
        if n > f:
            s.append(n)
            if len(s) == k:
                return s

        f = n
        if len(s) == k:
            s.sort(reverse=True)
            return s

    return s
