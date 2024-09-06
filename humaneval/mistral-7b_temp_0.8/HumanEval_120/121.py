
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

    # Initial solution
    # def maximum(arr, k):
    #     result = []
    #     for i in range(k):
    #         result.append(max(arr))
    #         arr.remove(max(arr))
    #     return result

    # Second solution
    # def maximum(arr, k):
    #     result = []
    #     arr.sort()
    #     result.append(arr[k - 1])
    #     arr.remove(arr[k - 1])
    #     for i in range(1, k):
    #         result.append(arr[-i])
    #     return result

    # Third solution
    # def maximum(arr, k):
    #     result = []
    #     arr.sort()
    #     result.append(arr[k - 1])
    #     arr.remove(arr[k - 1])
    #     for i in range(k - 2, -1, -1):
    #         result.append(arr[i])
    #     return result

