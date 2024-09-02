
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
    # sum, ans
    # for each num in arr
    #     if num < 10:
    #         sum += num
    #     elif num < 100:
    #         sum += num
    #     elif num < 1000:
    #         sum += num
    #     if k == 1:
    #         return ans
    #     k -= 1
    # return ans

    # sum = 0
    # k = min(k, len(arr))
    # for i in range(k):
    #     num = abs(arr[i])
    #     if num < 10:
    #         sum += num
    #     elif num < 100:
    #         sum += num
    #     elif num < 1000:
    #         sum += num
    # return sum

    # sum = 0
    # for i in range(len(arr)):
    #     if i >= k:
    #         break
    #     num = abs(arr[i])
    #     if num < 10:
    #         sum += num
    #     elif num < 100:
    #         sum += num
    #     elif num < 1000:
    #         sum += num
    # return sum

    # sum = 0
    # for i in range(k):
    #     num = abs(arr[i])
    #     if num < 10:
    #         sum += num
    #     elif num < 100:
    #         sum += num
    #     elif num < 1000:
    #         sum += num
    # return sum

    # sum = 0
    # for num in arr[:k]:
    #     if num < 10:
    #         sum += num
    #     elif num < 100:
    #         sum += num
    #     elif num < 1000:
    #         sum += num
    # return sum

    # sum = 0
    # k = min(k, len(arr))
    # for i in range
