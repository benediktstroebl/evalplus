import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # The idea is to keep two pointers: left and right, and slide them from left to right.
    # The minSubArraySum is the minimum value of subarray[left, right]
    # When the length of array is 0, the minSubArraySum is equal to the sum of the whole array

    min_sum = math.inf
    if not nums:
        return min_sum

    left = 0
    right = 0

    total = 0

    # move the right pointer until there are no elements left
    while right < len(nums):
        # add the element at the right pointer to the total
        total += nums[right]

        # expand the array to the right until it's bigger than min_sum
        while (right + 1) - left >= 1 and total >= min_sum:
            # the minimum sum is the total of the array at index left
            min_sum = total
            # move the left pointer to the right by one
            left += 1
            # subtract the element at the left pointer from the total
            total -= nums[left - 1]

        # increase the right pointer by one
        right += 1

    return min_sum
