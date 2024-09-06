
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
    arr = list(arr)
    n = len(arr)
    k = max(k,1)
    sum = 0
    for i in range(k,n+1):
        while i - k + 1 > 0 and arr[i-k+1] == arr[i-k+2] + arr[i-k+3]:
            i -= 1
            arr.remove(arr[i])
            arr.insert(0, arr[i])
            sum += arr[i-k+1]
        sum += arr[i-k+1]
    return sum
