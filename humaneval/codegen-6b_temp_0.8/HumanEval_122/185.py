
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
    digit = max(int(log10(arr[0])), int(log10(k)))
    max_digit = int(digit ** 2)

    for i in range(1, min(k, len(arr))):
        if log10(arr[i]) > digit:
            digit += 1
            max_digit += int(log10(arr[i]) ** 2) + 1

    return sum(arr[:max_digit])

