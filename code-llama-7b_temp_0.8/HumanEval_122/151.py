
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
    n = len(arr)
    if k >= n:
        return sum(arr)

    result = 0
    digits = 0
    curr_sum = 0
    for i in range(k):
        if arr[i] > 9:
            curr_sum += arr[i]
            digits += 1
        else:
            result += curr_sum
            curr_sum = arr[i]
            digits = 1

    if digits == 1:
        result += curr_sum
    else:
        result += curr_sum - 10**(digits - 1)

    return result

