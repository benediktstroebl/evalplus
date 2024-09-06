
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
    l, r = 0, k - 1
    max_element = max(arr[l:r+1])
    s = sum(arr[l:r+1])
    while max_element > 10:
        max_element //= 10
        l += 1
        r += 1
        if l > r:
            l, r = 0, k - 1
            max_element = max(arr[l:r+1])
            s = sum(arr[l:r+1])
    return s

