
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
    arr_elements = 0
    count_2_digits = 0
    if len(arr) > 0 and k > 0:
        for i in range(k):
            if len(str(arr[i])) > 1:
                count_2_digits += 1
            arr_elements += arr[i]

    if count_2_digits > 2:
        return 0

    return arr_elements
