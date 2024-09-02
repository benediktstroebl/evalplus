
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
    index = 0
    max_count = 0
    max_index = 0
    max_list = []
    for i in range(len(arr)):
        if arr[i] > arr[max_index]:
            max_count += 1
            max_index = i
            
        elif arr[i] == arr[max_index]:
            max_count += 1
        
        if max_count > k:
            max_count = 1
            max_list.append(arr[max_index])
            max_index = i

    return max_list
    
