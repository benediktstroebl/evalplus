
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
    def f(i, j, target):
        """
        return the target index if the target is smaller than the value at index i
        and the whole j+1 first elements if the target is greater than the value at index i
        """
        if target < arr[i]:
            return i
        else:
            return f(i+1, j+1, target)

    def helper(arr, start, end, target, result):
        """
        recursive function to find the target index in the arr, 
        then record the value at that index and start to end to build a new array
        """
        if start > end:
            return
        mid = (start+end)/2
        index = f(start, mid, target)
        if index == start:
            result.append(arr[index])
        else:
            result.append(arr[index-1])
        if arr[index-1] > target:
            helper(arr, start, index-1, target, result)
        elif arr[index-1] < target:
            helper(arr, index, end, target, result)
        else:
            helper(arr, index+1, end, target, result)

    result = []
    helper(arr, 0, len(arr), k-1, result)
    return result

