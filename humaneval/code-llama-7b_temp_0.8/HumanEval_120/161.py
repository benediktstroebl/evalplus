
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
    if not arr or k <= 0:
        return arr

    # Find the maximum element in arr[:k]
    max_val = max(arr[:k])

    # Find the first element in arr[:k] that is equal to max_val
    first_max_pos = arr[:k].index(max_val)

    # Prepend the first element in arr[:k] to the output.
    output = arr[first_max_pos:first_max_pos+1]

    # Find the maximum element in arr[k:]
    max_val = max(arr[k:])

    # Find the first element in arr[k:] that is equal to max_val
    first_max_pos = arr[k:].index(max_val) + k

    # Prepend the first element in arr[k:] to the output.
    output.append(arr[first_max_pos])

    return output

