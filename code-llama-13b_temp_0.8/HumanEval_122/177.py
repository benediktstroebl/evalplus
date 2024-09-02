
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
    arr_length = len(arr)
    digits = 0
    while digits < k and digits < arr_length:
        digits += (arr[digits] // 10) + 1
    return sum(map(lambda x: x if x < 100 else 0, arr[:digits]))

