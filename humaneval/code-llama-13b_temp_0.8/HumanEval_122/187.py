
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
    from collections import defaultdict

    map = defaultdict(int)

    for i, n in enumerate(arr):
        if i == k: break

        while n > 99:
            map[n % 100] += n % 10
            n /= 10

        while n > 9:
            map[n % 10] += n % 10
            n /= 10

        map[n] += n

    return sum(map.values())

