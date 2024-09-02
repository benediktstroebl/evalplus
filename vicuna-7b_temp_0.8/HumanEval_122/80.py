
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
    digit_sum = 0
    for i in range(1, k+1):
        digit_sum = str(digit_sum).zfill(2)
        for j in range(len(arr)):
            if len(str(arr[j])) <= 2:
                digit_sum += arr[j]
                break
        else:
            digit_sum += arr[j]
    return digit_sum