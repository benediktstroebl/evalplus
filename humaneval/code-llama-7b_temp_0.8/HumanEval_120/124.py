
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # set up an array of k size
    # insert into the array, sort the array
    # if we have the same values, take the first one (with the lower index)
    from collections import Counter
    counter = Counter(arr)
    from heapq import nlargest
    return nlargest(k, counter.keys(), key=counter.get)


    # ans = []
    # n = len(arr)
    # if k > n:
    #     return arr

    # for _ in range(k):
    #     max_val = -float("inf")
    #     for i in range(n):
    #         if arr[i] > max_val:
    #             max_val = arr[i]
    #             max_val_idx = i
    #     ans.append(arr[max_val_idx])
    #     arr.pop(max_val_idx)
    #     n -= 1
    # return ans

