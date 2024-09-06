
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
    # to store the sum of the elements with at most two digits
    sum_2_digit_elements = 0

    # iterate through the array using a for loop
    for i in range(k):
        # if the current element has 2 or less digits
        if len(str(arr[i])) <= 2:
            # add it to the sum
            sum_2_digit_elements += arr[i]

    return sum_2_digit_elements
