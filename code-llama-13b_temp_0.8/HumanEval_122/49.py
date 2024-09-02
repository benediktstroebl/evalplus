
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
    # TODO: figure out a more efficient solution
    if k >= len(arr):
        return sum([n for n in arr if 10 ** 2 > n >= 0])

    arr = sorted(arr)
    k = min(k, len(arr))
    sum_arr = sum(arr[0:k])
    new_sum = sum_arr
    for n in arr[0:k]:
        if n >= 10 ** 2:
            new_sum -= n

    return new_sum

