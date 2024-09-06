
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
    #  Create a list that will be returned.
    sorted_list = []

    #  If the length of the input list is less than the number of elements required,
    #  return the sorted list with all the input elements.
    if len(arr) < k:
        sorted_list = arr

    #  Otherwise, sort the input list in descending order.
    sorted_list = sorted(arr, reverse=True)

    #  Return the first k elements of the sorted list.
    return sorted_list[:k]

