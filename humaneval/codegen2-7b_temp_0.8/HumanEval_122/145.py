
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
    hash_map = {}
    for val in arr:
        sum = (val // 10) + (val % 10)
        if sum not in hash_map:
            hash_map[sum] = 1
        else:
            hash_map[sum] += 1
    for val in arr:
        if hash_map[val % 10] > 1:
            return val

