
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
    if len(arr) == 0:
        return 0
    elif len(arr) < k:
        return sum(arr)
    else:
        sum_of_elements = 0
        for i in range(0, k):
            sum_of_elements += arr[i]
        first_k_elemetns = arr[:k]
        for i in range(k, len(arr)):
            if len(str(arr[i])) <= 2:
                sum_of_elements += arr[i]
        return sum_of_elements

