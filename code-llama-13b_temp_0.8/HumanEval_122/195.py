
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

    def is_two_digits(n):
        return (abs(n) < 100)

    def sum_of_two_digit_numbers(arr, k):
        num = 0
        for i in range(k):
            if (is_two_digits(arr[i])):
                num += arr[i]
        return num

    return sum_of_two_digit_numbers(arr, k)

