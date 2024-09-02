
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
    for i in range(k):
        sum = 0
        for j in range(i, n+1):
            sum += arr[j]
        arr[i:j+1] = [sum//10] * (10 - (sum%10))
        sum = sum%10
        for j in range(k, n+1):
            if sum == 0:
                arr[j] = 0
            else:
                arr[j] = sum + arr[j]
    return arr
