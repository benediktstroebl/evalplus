
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
        if len(str(arr[i])) <= 2:
            count += arr[i]
    for i in range(k, len(arr)):
        if len(str(arr[i])) <= 2:
            count += arr[i]
    return count

assert(add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 5) == 15)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 10) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 1) == 15)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 2) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 3) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 4) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 5) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 6) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 7) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 8) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 9) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 10) == 22)
assert(add_elements([111,21,3,4000,5,6,7,8,9], 11) == 22)