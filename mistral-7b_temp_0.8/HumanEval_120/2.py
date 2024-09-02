
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

    # Create an empty list to store the top k elements
    top_k = []

    # Iterate over the array
    for num in arr:
        # If the list is empty or the current element is larger than the first element in the list,
        # append the current element to the list
        if not top_k or num > top_k[0]:
            top_k.append(num)
        # If the current element is less than the last element in the list, remove the last element
        # and append the current element
        elif num < top_k[-1]:
            top_k.pop()
            top_k.append(num)

    # If the list is longer than k, truncate it to k elements
    if len(top_k) > k:
        top_k = top_k[:k]

    return top_k

