
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
    # Solution:
    # 1. Collect the sums of the numbers with at most 2 digits
    # 2. Find the sum of the first k elements
    # 3. Subtract the second from the first
    # 4. Return the difference

    sums = []
    for num in arr:
        s = str(num)
        if len(s) <= 2:
            sums.append(num)
    return sum(sums[:k]) - sum(sums[k:])

