
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
    res = 0
    first_digits = []
    for num in arr[:k]:
        first_digits.append(num % 10)
        num //= 10

    second_digits = []
    for num in arr[:k]:
        second_digits.append(num % 100 // 10)
        num //= 10

    for i in first_digits:
        for j in second_digits:
            res += i + j

    return res
