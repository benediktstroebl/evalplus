
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
    # base case
    if len(arr) <= 0:
        return 0
    # traverse the input array till k
    # keep adding two digit elements
    total_sum = 0
    for i in range(k):
        val = arr[i]
        if val >= 10 and val < 100:
            total_sum += val
        else:
            print(i, val)
            total_sum += val % 10 + val // 10
    return total_sum

