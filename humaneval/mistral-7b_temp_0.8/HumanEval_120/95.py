
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
    def count_negative(arr):
        count = 0
        for i in arr:
            if i < 0:
                count += 1
        return count

    neg = count_negative(arr)
    if neg < k:
        return arr[:k]

    num = 0
    result = []
    for i in arr:
        if i > 0:
            num += 1
        if num >= k:
            if i > arr[k-1]:
                result.pop(k-1)
                result.append(i)
            else:
                break
        elif i < 0:
            num += 1
        else:
            result.append(i)
    return result






