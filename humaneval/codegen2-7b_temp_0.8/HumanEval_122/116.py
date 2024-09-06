
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
    size = len(arr)
    if k > size:
        return 0
    sum_arr = arr[:k]
    for i in range(k, size):
        sum_arr.append(arr[i])
        if len(set(str(sum_arr))) == 1:
            return sum(sum_arr)
    return sum_arr
