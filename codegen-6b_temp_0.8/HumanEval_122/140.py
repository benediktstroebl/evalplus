
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
    answer = 0
    prefix_sum = [0]

    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)

    for i in range(k + 1):
        answer += prefix_sum[min(i + 2, len(prefix_sum) - 1)] - prefix_sum[max(0, i - 1)]

    return answer

