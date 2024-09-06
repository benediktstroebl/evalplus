
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
    # corner case
    if k == 1:
        return sum(arr[:k])

    # get rid of all leading zeros
    arr = [i for i in arr if i != 0]

    ans = 0
    for i in range(0, len(arr), k):
        ans += sum(arr[i:i + k])
    return ans
