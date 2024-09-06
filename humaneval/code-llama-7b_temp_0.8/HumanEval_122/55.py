
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
    res = 0
    i = 0
    j = i + 1
    # ONLY TWO LOOPS are allowed (A bit tricky)
    # Mark down each element with its index
    for num in arr:
        num_str = str(num)
        if len(num_str) <= 2:
            res += num
        else:
            num_str = str(num)[:2]
            res += int(num_str)
        if j == k:
            break
        j += 1

    return res

