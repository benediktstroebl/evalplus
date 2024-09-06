
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
    # 1st brute force solution
    # O(k) time, O(k) space
    # time: k^2, space: k
    s = 0
    for i in range(k):
        t = 0
        for j in str(arr[i]):
            if len(j) > 0:
                t += int(j)
        s += t
    return s


    # 2nd solution, array sum
    # O(k) time, O(1) space
    # time: k, space: 1
    total = sum(arr[:k])
    ans = 0
    for num in arr[:k]:
        if num < 10:
            ans += num
        elif num < 100:
            ans += 1
        else:
            ans += 2
    return total - ans
