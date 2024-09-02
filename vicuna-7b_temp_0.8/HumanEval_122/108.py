
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
    arr_copy = arr[:]
    if len(arr) < k:
        return 0
    for i in range(k):
        arr_copy[i] = int(arr_copy[i].split(".")[0])
    while len(arr_copy) > k and arr_copy[-1] == 0:
        arr_copy.pop()
    result = 0
    for i in range(k):
        for j in range(i+1, len(arr_copy)):
            result += arr_copy[j] if (arr_copy[j].split(".")[0] <= '9') and (arr_copy[j].split(".")[0] < (arr_copy[j].split(".")[0].split(".")[0]) and (arr_copy[j].split(".")[0].split(".")[0] <= '9')) else (arr_copy[j] // 10)
    return result
