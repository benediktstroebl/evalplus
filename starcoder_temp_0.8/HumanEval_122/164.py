
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
    # First, make a dictionary.
    # Then, traverse through the dictionary and sum up values.
    # In the end, return that sum.
    ans = 0
    d = {}
    for i in range(k):
        d[arr[i]] = d.get(arr[i], 0) + 1
    for key in d:
        ans += key * min(2, d[key])
    return ans
