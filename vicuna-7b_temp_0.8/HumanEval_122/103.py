
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
    while i < k:
        if i == 0 and arr[i] == 0:
            while j < k and arr[j] == 0:
                j += 1
            while j < k:
                arr[j] = 0
                j += 1
        elif i == 0 and arr[i] == 1:
            j += 1
        else:
            arr[j] = arr[i]
            j += 1
            i += 1
    return sum(arr[j-1:])