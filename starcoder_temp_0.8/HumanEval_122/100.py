
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

    def _add_elements(arr, k):
        if len(arr) == 0:
            return 0
        if len(arr) <= 2:
            return sum(arr)

        first_digit = arr[0] // 10
        second_digit = arr[0] % 10

        if first_digit > 0:
            return _add_elements(arr[1:], k) + sum(arr[:k])
        else:
            if second_digit > 0:
                return _add_elements(arr[1:], k) + sum(arr[:2])
            else:
                return _add_elements(arr[1:], k)

    return _add_elements(arr, k)
