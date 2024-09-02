
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
    # n1 + n2 <= 99
    # n1 * n2 <= 999
    # n1 * n2 <= 999
    # n1 * n2 * n3 <= 9999
    # 9 * 9 * 9 * 9 <= 9999
    # 81 <= k <= 99
    # n1 <= 9

    # to avoid overflow, we need to substract 1 from the sum
    # if the number has more than two digits
    # this is a sum of products

    # total_sum = 0
    # for i in range(k):
    #     total_sum += arr[i]
    # print(total_sum)

    # let's do this with a single loop
    total_sum = 0
    for i in range(k):
        # if the digit is 10, need to subtract 1
        if arr[i] > 9:
            total_sum -= 1
        total_sum += arr[i]
    return total_sum

