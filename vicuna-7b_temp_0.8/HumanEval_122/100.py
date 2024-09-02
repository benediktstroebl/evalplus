
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
    if len(arr) < 1:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        res = 0
        for i in range(1, len(arr)):
            # Check if k is within range
            if i <= k <= i+1:
                res += arr[i]
            # Update the counter
            if i < k:
                k_digits = sum(1 for i in range(1, len(arr[i].split("")) if i in range(len(arr[i].split("")))))
                if k - i < k_digits:
                    k_digits = k - i
            else:
                k_digits = 0
        return res
