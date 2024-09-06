
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
    if k <= 0:
        return 0
    if len(arr) <= k:
        return sum(arr)

    arr.sort(key=lambda x: x%100)

    # O(n)
    def get_unique(arr):
        hash = {}
        for i in arr:
            if i not in hash:
                hash[i] = 1
        return hash.keys()

    # O(n)
    unique_values = get_unique(arr[:k])

    # O(n)
    def get_sum(arr, values):
        hash = {}
        for i in values:
            hash[i] = arr.count(i)
        return sum(hash.keys())

    return get_sum(arr[:k], unique_values)


