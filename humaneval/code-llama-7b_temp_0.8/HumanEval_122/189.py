
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
    answer = 0
    k_digits = set()
    for a in arr[:k]:
        k_digits.add(a % 10)
        k_digits.add(a // 10)
    for a in arr:
        if len(k_digits) >= 2:
            break
        if a % 10 in k_digits and a // 10 in k_digits:
            answer += a
    return answer

