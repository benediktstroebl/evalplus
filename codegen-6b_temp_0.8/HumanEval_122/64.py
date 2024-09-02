
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
    result = sum(map(int, map(str, arr[:k])))
    for n in arr[k:]:
        result += n // 10
        result += n % 10
    return result


assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
assert add_elements([111, 111, 222, 444, 444, 555], 4) == 46
assert add_elements([111, 222, 666, 666, 666, 666], 4) == 74
assert add_elements([111, 222, 333, 444, 555], 4) == 74
assert add_elements([111, 222, 333, 444, 555], 8) == 33
assert add_elements([111, 222, 333, 444, 555], 10) == 0

