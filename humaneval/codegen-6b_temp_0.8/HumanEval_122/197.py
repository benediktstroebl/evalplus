
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
    if arr is None:
        return 0

    arr_sum = sum(arr[:k])
    arr_digits = set()
    for num in arr[:k]:
        arr_digits.add(int(num/10))

    for num in arr[k:]:
        if num % 10 in arr_digits:
            arr_sum += num
        arr_digits.add(int(num/10))

    return arr_sum

