
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
    # convert to list of single digits
    arr_digits = [int(d) for d in arr]
    # store the sum of digits with at most 2 digits in a new array
    sum_arr = [0] * n
    for i in range(k, n):
        sum_arr[i-k] = sum_arr[i-k] + arr_digits[i]
    # return the sum of digits with at most 2 digits from the first k elements of arr
    return sum([d for d in sum_arr if len(str(d)) <= 2])