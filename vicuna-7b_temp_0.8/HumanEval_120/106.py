
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
    def partition(arr, i, j):
        """
        Partition the arr such that the first i numbers are less than or 
        equal to each number in arr[j:].

        Parameters:
        - arr: an array of integers
        - i: an integer
        - j: an integer

        Returns:
        - None
        """
        left = 0
        right = j
        while left <= i:
            if arr[right] < arr[left]:
                break
            right += 1
        while right <= j:
            arr[left] = arr[right]
            left += 1
            right += 1
    partition(arr, 0, len(arr) - 1)
    if k == 0:
        return []
    elif k == 1:
        return [arr[0]]
    else:
        return arr[:k]