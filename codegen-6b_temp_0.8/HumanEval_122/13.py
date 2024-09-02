
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
    i, j = 0, k
    while k > 0:
        if arr[i] <= 9:
            k -= 1
            i += 1
        else:
            break

    while i < len(arr) and j < len(arr):
        if arr[i] < 10:
            k -= 1
            i += 1
        elif arr[j] < 10:
            j += 1
            k -= 1
        else:
            break

    j = j if j < len(arr) else 0
    return sum(arr[i:j])

