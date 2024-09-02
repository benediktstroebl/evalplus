
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
    # idea: use monotonic stack with length at most 2

    stack = []
    i = 0
    while i < k:
        while stack and stack[-1] < arr[i]:
            stack.pop()
        stack.append(arr[i])
        i += 1

    summ = 0
    while stack and stack[-1] < 100:
        summ += stack[-1]
        stack.pop()

    return summ

