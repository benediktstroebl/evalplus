
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
    prefix_sum = [0]
    for i in arr:
        prefix_sum.append(prefix_sum[-1] + i)
    output = 0
    for i in range(len(arr)):
        if i < k:
            output += prefix_sum[i+k] - prefix_sum[i]
        else:
            output += prefix_sum[i+k] - prefix_sum[i] - prefix_sum[i-k] + prefix_sum[i-k-1]
    return output
