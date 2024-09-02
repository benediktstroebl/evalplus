
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
    sum = 0
    for i in range(n):
        while(arr[i] >= 1000):
            arr[i] -= 1000
            i -= 1
            if i < 0:
                break
        while(arr[i] >= 100):
            arr[i] -= 100
            i -= 1
            if i < 0:
                break
        sum += arr[i]
    return sum