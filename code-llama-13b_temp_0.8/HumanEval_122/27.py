
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
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
    max_sum = 0
    min_sum = 0

    for index in range(k):
        if arr[index] < digits[1]:
            min_sum += arr[index]
        elif arr[index] < digits[10]:
            min_sum += digits[1]
            max_sum += digits[10] - arr[index]
        else:
            max_sum += digits[10]

    return min_sum + max_sum

