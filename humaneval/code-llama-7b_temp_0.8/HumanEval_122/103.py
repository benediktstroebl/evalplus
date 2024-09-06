
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
    if not arr or k >= len(arr):
        return 0

    if k == 0:
        return 0

    answer = sum(map(int, str(arr[0]))) if len(str(arr[0])) <= 2 else arr[0]

    for i in range(1, k):
        answer += add_elements(arr[1:], i)

    return answer
