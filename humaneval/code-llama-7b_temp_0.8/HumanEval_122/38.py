
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
    if len(arr) == 0 or k == 0:
        return 0

    limit = 10**2

    accumulator = 0
    first = 0
    last = first + k
    while last <= len(arr):
        # compute sum of first k elements
        if last == len(arr):
            last -= 1
        current = 0
        for i in range(first, last):
            current += arr[i]
            # check if current is in bounds
            if current >= limit:
                break
        # if found, accumulate and advance first
        if current < limit:
            accumulator += current
            first += 1
        # else advance last
        else:
            last += 1
    return accumulator
