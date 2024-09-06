
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
    if not arr:
        return 0
    count = 0
    for num in arr:
        while num > 99:
            num -= 100
            count += 1
        if num > 9:
            num -= 10
            count += 1
        count += num
        k -= 1
        if k == 0:
            break
    return count

