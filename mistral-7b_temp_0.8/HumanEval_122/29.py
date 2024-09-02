
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

    # Solution 1 (linear)
    # time: O(n)
    # space: O(1)
    sum = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]

    return sum

    # Solution 2 (linear)
    # time: O(n)
    # space: O(n)
    # Answer array with the same len of arr
    ans = [0] * len(arr)

    for i in range(k):
        if len(str(arr[i])) <= 2:
            ans[i] = arr[i]

    return sum(ans)
