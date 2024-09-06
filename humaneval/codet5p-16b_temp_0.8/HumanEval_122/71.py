
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

    i, j, sum, temp = 0, k, 0, 0

    while i < j:
        temp = arr[i] + arr[j]

        if temp > 9:
            sum += temp - 10
            temp = 1

        sum += temp
        i += 1
        j -= 1

    if i == k and temp > 0:
        sum += temp

    return sum

