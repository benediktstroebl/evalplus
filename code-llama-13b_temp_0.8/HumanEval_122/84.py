
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

    ### Method 1: Manual checks for digits

    # # find the first k elements
    # # print(arr[:k])

    # # keep track of sums of 2 digit elements
    # sum_2_digit = 0

    # # loop through first k elements
    # for i in range(0, k):
    #     # convert the integer to a string
    #     element_as_string = str(arr[i])
    #     # print(element_as_string)

    #     # check if the string has 2 characters
    #     if len(element_as_string) == 2:
    #         sum_2_digit += int(element_as_string)

    # # print(sum_2_digit)
    # return sum_2_digit

    ### Method 2: Normalization

    # convert the integer to a string
    arr = [str(element) for element in arr]

    # loop through first k elements
    sum_2_digit = 0
    for i in range(0, k):
        # check if the string has 2 characters
        if len(arr[i]) == 2:
            sum_2_digit += int(arr[i])

    return sum_2_digit

