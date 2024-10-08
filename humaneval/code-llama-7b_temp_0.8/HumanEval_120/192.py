
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
    def nth_element(arr, k):
        """
        This algorithm uses QuickSelect to find the kth smallest element.

        This algorithm has a worst-case time complexity of O(n^2) where n is 
        the size of the input array, but it is very fast in practice.
        """
        n = len(arr)
        if n == k: return
        pivot = arr[(n-1)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        n_left = len(left)
        n_middle = len(middle)
        n_right = len(right)

        if k < n_left:
            return nth_element(left, k)
        elif k < n_left + n_middle:
            return pivot
        else:
            return nth_element(right, k - n_left - n_middle)

    max_num = nth_element(arr, k)
    return [x for x in arr if x == max_num]
