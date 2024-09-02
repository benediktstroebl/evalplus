
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
        # sum of the elements with at most two digits
        sum = 0
        for j in range(i, len(arr)):
            # the sum is the sum of the digits of arr[j]
            digit = 0
            while (arr[j] > 0):
                digit = digit * 10 + (arr[j] % 10)
                j = j - 1
            sum = sum + digit
        # if k is greater than the first digit of arr[0]
        if i == 0:
            arr = arr[:i] + [sum] + arr[i:]
        else:
            arr = arr[:i] + [sum]
    return arr