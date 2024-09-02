
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

    max_digits = 0
    for num in arr:
        num_digits = 0
        while num > 0:
            num //= 10
            num_digits += 1

        max_digits = max(max_digits, num_digits)

    if max_digits <= k:
        return sum(arr)

    if k == 1:
        return sum(x for x in arr if x >= 10)

    return sum(x for x in arr[:k] if x >= 10) + sum(x for x in arr[k:] if x < 10)

