
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

    # Time Complexity: O(NlogN)
    # Space Complexity: O(logN)

    # We're given an array of integers and a positive integer k, and we need to return a sorted list of length k with the maximum k numbers in the array.

    # First, we can use the heapq module to implement a min heap. Then, we can extract the k largest elements from the array using the heapify function.

    # Finally, we can return the sorted list of length k.

    # import heapq

    # def maximum(arr, k):
    #     heapq.heapify(arr)
    #     return [heapq.nsmallest(k, arr)]

    # Second, we can use the min heap to get the k largest elements.

    # We first sort the array in descending order and then get the first k elements.

    # import heapq

    # def maximum(arr, k):
    #     return sorted(arr, reverse=True)[:k]

    # Third, we can use the merge sort to get the k largest elements
