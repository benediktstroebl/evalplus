
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
    if k >= len(arr):
        return arr
    
    start_index, end_index = 0, k
    while end_index <= len(arr):
        current_slice = arr[start_index:end_index]
        current_max = max(current_slice)
        if current_max == -float('inf'):
            break
        else:
            max_index = arr.index(current_max)
            if max_index < start_index:
                break
            else:
                start_index = max_index + 1
                end_index += 1

    return arr[start_index:end_index]

assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum([4, -4, 4], 2) == [4, 4]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]

