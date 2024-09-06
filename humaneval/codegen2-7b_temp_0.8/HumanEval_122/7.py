
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
    for i in range(len(arr)):
        if arr[i] % 10 == k:
            arr[i] += arr[i - 1]
        elif arr[i] >= 10 and arr[i] <= 99:
            arr[i + 1] += arr[i] // 10
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    return sum(arr[:k])
