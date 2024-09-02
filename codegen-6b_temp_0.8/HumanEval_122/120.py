
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
    i = 0
    j = 0
    count = 1
    while count < k:
        if (j + 1 < len(arr) and int(str(arr[j])[0]) <= 3) or j == len(arr) - 1:
            j += 1
        else:
            j += 1
            i += 1
            count += 1
    return sum(arr[i:j + 1])

