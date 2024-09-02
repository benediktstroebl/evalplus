
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

    # 1st solution
    # O(n) time | O(1) space

    # To solve this problem, I use the variable two_digit_sum to store the sum of the
    # two-digit numbers in the first k elements of the array. At the end of the loop,
    # I will return two_digit_sum + sum(arr[k:]) to get the result.

    # Two things to note: the base case is when k is equal to 0. In this case,
    # the two_digit_sum is 0 and we will return 0.

    # The second thing to note is the algorithm of the loop. The loop keeps track
    # of the sum of the two-digit numbers in the first k elements of the array.
    # When k is not 0, it will use a variable sum to calculate the sum of the
    # two-digit numbers in the first k elements of the array.

    # When k is not 0, the algorithm is the following:
    # If arr[k - 1] is less than 100, sum is equal to sum + arr[k - 1]. This means
    # that the current two-digit number is part of the sum.
    # Otherwise, sum is equal to sum - arr[k - 1] + 10 * (arr[k - 1] % 100), which
    # is the difference of the current two-digit number and the previous two-digit
    # number, minus 100 (the number of the two-digit numbers in arr[k - 1]).

    # The reason for subtracting 100 is that when we use the modulo (%) operator,
    # the two-digit number will be the remainder of the division (//). For example,
    # 400 % 100 = 4, but the two-digit number we are looking for is 400, not 4.
    # The solution is to first subtract 100 from arr[k - 1] to get the two-digit
    # number. We can then use the modulo (%) operator to calculate the remainder of
    # the division (//) and get the two-digit number.
