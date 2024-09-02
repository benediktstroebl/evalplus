
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
    stack = []
    i = 0
    while i < k:
        top = -1
        if len(stack) == 0:
            for j in range(i, len(arr)):
                stack.append(arr[j])
                top = j
        else:
            for j in range(len(arr)):
                if stack[-1] > arr[j]:
                    stack.pop()
                    stack.append(arr[j])
                    top = j
        i = top + 1
    return
