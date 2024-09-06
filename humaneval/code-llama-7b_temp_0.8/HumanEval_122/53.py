
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
    def num_digits(n):
        if n == 0:
            return 1
        return int(math.log10(n)) + 1

    prefix_sum = [0]
    for elem in arr:
        prefix_sum.append(prefix_sum[-1] + elem)

    res = 0
    for i in range(k):
        for j in range(i + 1, k + 1):
            res += prefix_sum[j] - prefix_sum[i]
            if num_digits(j - i) > 2:
                break
    return res

    # # Time complexity O(k*n)
    # # Space complexity O(n)
    # left, right = 0, k
    # count_digits = [0] * 10
    # for i in range(right, len(arr)):
    #     count_digits[arr[i] % 10] += 1
    # res = 0
    # for i in range(left, right):
    #     if count_digits[arr[i] // 10] == 0:
    #         res += arr[i]
    #     if count_digits[arr[i] % 10] > 0:
    #         res += arr[i] * count_digits[arr[i] % 10]
    # return res
