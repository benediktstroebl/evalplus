
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    # Explanation:
    # * Take two pointers at the beginning of the array.
    # * While at least one pointer is less than or equal to k,
    #   add the two values to the sum, increment the first pointer,
    #   and decrement the second.
    # * Return the sum.

    # Time complexity: O(k)
    # Space complexity: O(1)

    k = min(k, len(arr))
    return sum(arr[i] + arr[j] for i, j in zip(range(k), range(k-1, -1, -1)))
