
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
    from collections import Counter

    def hash(num):
        return num // 10, num % 10

    count = Counter([hash(num) for num in arr[:k]])
    ans = 0
    for i in range(k):
        ans += (i + 1) * count[hash(arr[i])]
        if arr[i] // 100!= 0:
            ans += count[hash(arr[i] // 100)]
    return ans

