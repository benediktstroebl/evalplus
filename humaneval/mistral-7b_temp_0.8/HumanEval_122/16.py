
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
    def get_sum(k, i):
        if k == i:
            return arr[i]
        else:
            return arr[i] + get_sum(k, i + 1)

    def get_digits(x):
        return len(str(x))

    sum_two_digits = 0
    for i in range(len(arr)):
        if get_digits(arr[i]) <= 2:
            sum_two_digits += arr[i]

    return sum_two_digits

