
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
    cnt = 0
    for i in range(0,len(arr)-k+1):
        s = arr[i:i+k]
        if len(str(int(s[0]))) <= 2 and len(s) > 1:
            cnt += int(s[0])
    return cnt
