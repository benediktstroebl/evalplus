
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
    # left pointer
    left = 0

    # keep the window size
    window_size = 2

    # hashmap for two digit numbers
    two_digit_nums = {}

    # sum of the numbers
    sum_of_nums = 0

    # while the window has not reached k
    while left < k:

        # iterate over the window
        for i in range(left, left + window_size):

            # update the window size and window sum
            window_size = i - left + 1
            sum_of_nums += arr[i]

            # check if the number has two digits
            if len(str(arr[i])) == 2:

                # add it to the hashmap
                two_digit_nums[arr[i]] = two_digit_nums.get(arr[i], 0) + 1

        # update the window
        left += 1

    # return the sum minus the two digit numbers
    return sum_of_nums - sum(two_digit_nums.values())

