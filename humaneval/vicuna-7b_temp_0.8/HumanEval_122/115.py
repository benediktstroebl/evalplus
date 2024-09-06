
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
    for i in range(k):
        j = k - i
        while j >= 0:
            if (arr[j] > 9):
                arr[j] = arr[j] - 10
                j -= 1
            elif arr[j] > 0:
                arr[j] = arr[j] - 1
                j -= 1
            else:
                break
    return arr