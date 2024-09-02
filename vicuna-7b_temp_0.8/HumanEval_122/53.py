
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
    from itertools import combinations

    # using k as index
    for i in range(1, len(arr) + 1):
        for j in range(i, len(arr)):
            # using combinations(range(1, k + 1), i + 1)
            # Combinations(range(1, k + 1), i + 1)
            for comb in combinations(range(1, k + 1), i + 1):
                sum = 0
                for _ in comb:
                    sum += arr[j - i]
                if len(str(sum)) <= 2:
                    return sum

    return 0