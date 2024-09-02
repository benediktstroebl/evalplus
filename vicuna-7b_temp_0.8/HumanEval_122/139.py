
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
    if k >= len(arr):
        return 0
    sum = 0
    for i in range(1, k + 1):
        while i < len(arr):
            if len(str(arr[i])) <= 2:
                sum += arr[i]
                i += 1
        if sum == 0:
            sum += arr[k]
        if len(str(arr[i-1])) == 2 and len(str(arr[i])) == 2:
            sum -= int(arr[i-1])
        if sum == 0:
            sum += int(arr[i])
    return sum