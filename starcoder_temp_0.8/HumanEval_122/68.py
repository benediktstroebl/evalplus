
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

    # Note: This solution is not optimal. It is O(n) in time and space.
    # You can use more space to make it O(1) or to make it better.

    # if k >= 2:
    #     max_2_digit = 99
    #     max_1_digit = 9
    # else:
    #     max_2_digit = 99 % 100
    #     max_1_digit = 9 % 10
    #     if k >= 1:
    #         max_1_digit += 1
    #     else:
    #         max_1_digit = 0
    # return sum(x for x in arr[:k] if x <= max_2_digit) + sum(x for x in arr[:k] if x <= max_1_digit)

    # if k >= 2:
    #     max_2_digit = 99
    #     max_1_digit = 9
    # else:
    #     max_2_digit = 99 % 100
    #     max_1_digit = 9 % 10
    #     if k >= 1:
    #         max_1_digit += 1
    #     else:
    #         max_1_digit = 0
    # return sum(x for x in arr[:k] if x <= max_2_digit) + sum(x for x in arr[:k] if x <= max_1_digit)

    if k >= 2:
        max_2_digit = 99
        max_1_digit = 9
    else:
        max_2_digit = 99 % 100
        max_1_digit = 9 % 10
        if k >= 1:
            max_1_digit += 1
        else:
            max_1_digit = 0
    return sum(x for x in arr[:k] if x <= max_2_digit) + sum(x for x in arr[:k] if x <= max_1_digit)
