
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

    # Given a non-empty array of integers arr and an integer k, return
    # the sum of the elements with at most two digits from the first k elements of arr.

    # Example:

    # Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
    # Output: 24 # sum of 21 + 3

    # Constraints:

    # 1. 1 <= len(arr) <= 100
    # 2. 1 <= k <= len(arr)

    # Assume arr is sorted
    # base case
    if k == 1:
        return arr[0]

    total = 0
    # total up all elements if the first digit is less than 2
    if arr[k - 1] // 10 < 2:
        total += sum(arr[:k])
    else:
        total += sum(arr[:2])

    # recursive case
    return total + add_elements(arr[2:], k - 2)


