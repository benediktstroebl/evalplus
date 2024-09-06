
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
    if not arr:
        return arr

    max_values = []
    while len(max_values) < k:
        # this is to find the minimum value in arr, it is used as the pivot
        # to find the left and right parts of the array
        max_value = min(arr)

        # find the right part of the array
        left_part, right_part = [], []
        i = 0
        while i < len(arr):
            if arr[i] < max_value:
                left_part.append(arr[i])
            else:
                right_part.append(arr[i])
            i += 1

        # find the median (i.e. the median index) of the right part
        mid = len(right_part) // 2
        if len(right_part) % 2:
            mid = mid + 1
        mid_value = right_part[mid]

        # the max number can only exist in the left part
        max_values.append(max_value)

        # the left part is a valid array
        if left_part:
            # if the left part has more than k numbers,
            # then just add the left_part to the max_values
            if len(left_part) > k:
                max_values += left_part[:k]
                break
            # if the left part has equal or less to k numbers,
            # then the left_part is the max_value of the left_part
            else:
                max_value = left_part[-1]
                max_values.append(max_value)

        # the right part is the max_value of the left part
        max_values.append(mid_value)

        # the right part is a valid array
        if right_part:
            if len(right_part) > k:
                max_values += right_part[:k]
                break
            else:
                max_value = right_part[-1]
                max_values.append(max_value)

        # update the arr
        arr = [max_value] + left_part + right_part[::-1]

    return max_values


assert