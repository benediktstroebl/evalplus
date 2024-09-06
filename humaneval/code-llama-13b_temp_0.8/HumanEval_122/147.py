
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
    # in case of two digit numbers, return 2 digit sum + digit 1 + digit 2
    # if there is only one digit, return that single digit
    # if there is no digit, return 0
    # The time complexity is O(k), the space complexity is O(1)
    # 158ms, 24.9MB
    return sum([sum(map(int, str(i))) if i >= 10 else i for i in arr[:k]])

