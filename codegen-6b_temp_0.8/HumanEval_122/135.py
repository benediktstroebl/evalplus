
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

    for i in range(k):
        res += arr[i]

    idx = k
    while idx < len(arr):
        if arr[idx] < 10:
            res += arr[idx]
        else:
            res += arr[idx] % 10 + arr[idx] // 10
        idx += 1

    return res


assert(add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24)
assert(add_elements([42], 1) == 43)
assert(add_elements([], 1) == 0)
assert(add_elements([], 0) == 0)
assert(add_elements([10, 1], 1) == 11)
assert(add_elements([10, 11, 2, 3, 43, 4], 3) == 19)
assert(add_elements([1, 1, 1, 3, 3, 3, 3], 1) == 22)
assert(add_elements([2, 2, 2, 3, 4, 5, 5], 0) == 15)
assert(add_elements([3, 3, 3, 3, 4, 5, 5], 1) == 19)
assert(add_elements([3, 3, 3, 3, 4, 5, 5], 2) == 19)
assert(add_elements([3, 3, 3, 3, 4, 5, 5], 3) == 19)
assert(add_elements([3, 3, 3, 3, 4, 5, 5], 4) == 19)
assert(add_elements([3, 3, 3, 3, 4, 5, 5], 5) == 19)
