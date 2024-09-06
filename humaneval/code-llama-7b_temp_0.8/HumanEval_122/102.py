
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
    # import sys
    # sys.setrecursionlimit(1500)
    # result = []
    # def dfs(i, sum, digits):
    #     if i == len(arr):
    #         result.append(sum)
    #         return
    #     if digits >= 3:
    #         return
    #     num = str(arr[i])
    #     if len(num) <= 2:
    #         sum += arr[i]
    #         dfs(i+1, sum, digits+1)
    #         dfs(i+1, sum, digits)
    #     else:
    #         dfs(i+1, sum, digits)
    # dfs(0, 0, 0)
    # return max(result)

    # import sys
    # sys.setrecursionlimit(1500)
    # result = []
    # def dfs(i, sum, digits):
    #     if i == len(arr):
    #         result.append(sum)
    #         return
    #     if digits >= 3:
    #         return
    #     num = str(arr[i])
    #     if len(num) <= 2:
    #         sum += arr[i]
    #     dfs(i+1, sum, digits + (len(num) <= 2))
    # dfs(0, 0, 0)
    # return max(result)

    # import sys
    # sys.setrecursionlimit(1500)
    # def dfs(i, sum, digits):
    #     if i == len(arr):
    #         return sum
    #     if digits >= 3:
    #         return 0
    #     num = str(arr[i])
    #     if len(num) <= 2:
    #         return dfs(i+1, sum+arr[i], digits+1)
    #     else:
    #         return dfs(i+1, sum, digits)
    # return max([dfs(0, 0, 0), dfs(0,
