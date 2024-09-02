
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
    p1, p2 = 0, k - 1
    total = 0
    while p1 <= p2:
        if 10 <= arr[p1] <= 99:
            total += arr[p1]
            p2 -= 1
        else:
            total += arr[p1]
        p1 += 1

    return total
