
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
    # Edge cases
    if len(arr) == 1:
        return arr[0]
    if len(arr) < k:
        return 0

    # Define variables
    # running_sum: sum of elements seen so far
    # cur_sum: current sum of all elements starting from first
    #           k elements of arr
    # two_dig_sum: sum of all elements seen so far with two digits
    # last_dig: digits of last element seen
    running_sum = 0
    cur_sum = 0
    two_dig_sum = 0
    last_dig = None

    # Loop through first k elements of arr
    for i in range(k):
        cur_sum += arr[i]
        two_dig_sum += two_digits(arr[i])

    # Update running_sum and last_dig
    running_sum = cur_sum
    last_dig = last_digit(arr[k - 1])

    # Loop through all other elements of arr
    for i in range(k, len(arr)):
        # Remove first digit from cur_sum
        cur_sum -= arr[i - k]

        # Add last digit from arr[i] to cur_sum
        cur_sum += last_digit(arr[i])

        # Update two_dig_sum with new two-digit number
        two_dig_sum += two_digits(last_dig * 10 + last_digit(arr[i]))

        # Update last_dig
        last_dig = last_digit(arr[i])

        # Update running_sum
        running_sum = max(running_sum, cur_sum)

    return running_sum + two_dig_sum
