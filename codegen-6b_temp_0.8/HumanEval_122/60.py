
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
    n = len(arr)
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[i] + arr[i])

    prefix_sum = prefix_sum[1:-1]

    result = 0
    for i in range(k):
        a, b = divmod(prefix_sum[i], 10)
        result += a*10**(i) + b*10**(i+1) + b*10**i
    return result

