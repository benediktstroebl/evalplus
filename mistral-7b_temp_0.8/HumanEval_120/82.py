
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
    # 1st way
    # 1. Sort the array and return the first k elements.
    # 2. Use heap sort to return the k largest elements.
    # 3. Use quick select to return the kth largest element.
    # 4. Use quick select to return the k smallest elements.

    def quick_select(arr, k):
        """
        Select the kth largest element in the array arr.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(arr) - 1

        while left < right:
            p = partition(arr, left, right)

            if p == k:
                return arr[p]
            elif p > k:
                right = p - 1
            else:
                left = p + 1

        return arr[p]

    def partition(arr, left, right):
        """
        Partition the array arr between the elements at indices left and right.

        Time complexity: O(n)
        Space complexity:
