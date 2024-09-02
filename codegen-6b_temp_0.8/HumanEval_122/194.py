
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
    count = 0
    for i in range(k):
        a = arr[i]
        if a < 10 or a > 99:
            count += a
    for j in range(k, len(arr)):
        a = arr[j]
        if a < 10 or a > 99:
            count += a
    return count


assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24, add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
assert add_elements([1, 2, 3], 3) == 6, add_elements([1, 2, 3], 3)
assert add_elements([1], 1) == 1, add_elements([1], 1)
assert add_elements([18, 19, 22, 3, 4], 4) == 51, add_elements([18, 19, 22, 3, 4], 4)
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 55, add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
assert add_elements([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22], 19) == 113, add_elements([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22], 19)
assert add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22], 19) == 113, add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22], 19)
assert add_elements([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,