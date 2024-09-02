
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
    total = 0
    # we'll have two indexes, one for the left, one for the right,
    # and then we'll check if the value at the left index is less than
    # or equal to the maximum allowed digits, and then we'll check
    # if the sum of the value at the left index and the value at the
    # right index is greater than or equal to the maximum allowed digits
    # if both of these conditions are true, then we add the values at
    # the left and right indices together to the total
    left, right = 0, 0
    while right < len(arr):
        left_val = arr[left]
        right_val = arr[right]

        if left_val <= k and left_val + right_val >= k:
            total += left_val + right_val

        right += 1
        # if we've reached the end of the array and the right value
        # isn't greater than the maximum allowed digits, then we'll
        # reset the right value to the left value
        if right == len(arr) and right_val <= k:
            right = left

        left += 1
        # if we've reached the end of the array and the left value
        # isn't greater than the maximum allowed digits, then we'll
        # reset the left value to the right value
        if right == len(arr) and left_val <= k:
            left = right

    return total
