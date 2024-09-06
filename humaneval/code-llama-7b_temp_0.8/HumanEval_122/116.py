
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
    length = len(arr)

    if length == 1:
        return arr[0]

    # two pass.
    # 1. prefix sum.
    # 2. solution.
    psum = [0] * length
    psum[0] = arr[0]
    for i in range(1, length):
        psum[i] = psum[i-1] + arr[i]

    return psum[k-1] + sum(arr[k:])

