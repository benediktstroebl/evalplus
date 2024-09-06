
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
    # Initialization
    m = {}
    for i in range(k):
        if arr[i] not in m or m[arr[i]] < i:
            m[arr[i]] = i
    
    # Loop through the array and push out the items that are not in the top k
    for i in range(k, len(arr)):
        if arr[i] in m and m[arr[i]] == i:
            m[arr[i]] = i
        else:
            j = i
            while j > k-1 and arr[j] in m and m[arr[j]] <= j:
                j -= 1
            
            m[arr[j]] = j
    
    # Output the top k items
    res = [-1] * k
    for i in range(k):
        res[i] = max(m)
        m.pop(res[i])
    
    return res

