
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
    counts = [0 for i in range(10)]

    for i in range(k):
        counts[int(arr[i])] += 1

    for i in range(10):
        if counts[i] == 0:
            continue
        elif counts[i] <= 2:
            return sum(arr[:k])
        else:
            break
    return sum(arr[:k] + arr[k+1:]) + sum(arr[k:])
