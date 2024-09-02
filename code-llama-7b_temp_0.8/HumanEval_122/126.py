
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
    ans = 0
    curr = []
    for i in range(k):
        curr.append(arr[i])

    for elem in curr:
        if len(str(elem)) <= 2:
            ans += elem
    
    for i in range(k, len(arr)):
        curr.pop(0)
        curr.append(arr[i])
        if len(str(curr[len(curr) - 1])) <= 2:
            ans += curr[len(curr) - 1]

    return ans
