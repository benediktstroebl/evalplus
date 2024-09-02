
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
    # res = 0
    # for i in range(k):
    #     element = arr[i]
    #     if element > 99:
    #         element = 99
    #     elif element < -99:
    #         element = -99
    #     res += element
    # return res

    if k >= len(arr):
        return 0
    return sum(arr[:k]) - (sum(num > 99 or num < -99 for num in arr) * 99)

