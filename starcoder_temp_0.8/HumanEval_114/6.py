import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    def divide_and_conquer(start, end):
        if start == end:
            return nums[start]
        mid = int((start + end) / 2)
        left_sum = divide_and_conquer(start, mid)
        right_sum = divide_and_conquer(mid + 1, end)
        total = 0
        left, right = mid, mid + 1
        left_min, right_min = nums[mid], nums[mid + 1]
        while left >= start and right <= end:
            if nums[left] + nums[right] < left_min + right_min:
                total = left_min + right_min
                left -= 1
            else:
                right_min = nums[right]
                right += 1
        total += sum(nums[left + 1:right])
        return min(left_sum, right_sum, total)

    return divide_and_conquer(0, len(nums) - 1)
