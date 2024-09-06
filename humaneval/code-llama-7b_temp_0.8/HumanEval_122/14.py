
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
    def num_digits(num):
        if num < 10:
            return 1
        else:
            return 1 + num_digits(num // 10)

    def two_digits_from_begin(arr, k):
        if k < 2:
            return 0
        else:
            return arr[k - 1] + two_digits_from_begin(arr, k - 2)

    def two_digits_sum_from_begin(arr, k):
        if k < 2:
            return 0
        else:
            return arr[k - 1] + two_digits_sum_from_begin(arr, k - 2)

    num_digits_arr = [num_digits(elem) for elem in arr]
    num_digits_begin_two = two_digits_from_begin(num_digits_arr, k)
    num_digits_sum_begin_two = two_digits_sum_from_begin(num_digits_arr, k)

    return (num_digits_arr[k - 1] - num_digits_begin_two) * 10 + num_digits_sum_begin_two
