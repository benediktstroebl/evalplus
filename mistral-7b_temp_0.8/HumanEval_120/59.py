
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
    if len(arr) == 0:
        return None
    elif k == 0:
        return []
    elif k == 1:
        return [arr[0]]

    # Create an empty list to store the maximum numbers
    max_nums = []

    # Traverse the array from the beginning to the end
    for i in range(len(arr)):
        # If the current number is greater than the maximum number in the list,
        # replace the maximum number with the current number and remove any duplicate numbers
        if arr[i] > max_nums[-1]:
            max_nums.append(arr[i])
        elif len(max_nums) < k:
            max_nums.append(arr[i])
        else:
            max_nums.sort()
            max_nums.remove(max_nums[0])
            max_nums.append(arr[i])

    # Return the sorted list of maximum numbers
    return max_nums[:k]

