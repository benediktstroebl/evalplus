import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # SUM OF ALL INTEGERS DIVIDED BY 2

    # sample code
    # def integerDivision(self, a):
    #     l = len(a)
    #     a_sum = sum(a)
    #     res = a_sum
    #     for i in range(l):
    #         a_sum -= a[i]
    #         res = min(res, a_sum)
    #     return res

    # return integerDivision(nums)

    # sample code
    # def sumOddLengthSubarrays(self, a):
    #     l = len(a)
    #     res = 0
    #     for i in range(l):
    #         for j in range(i, l, 2):
    #             res += sum(a[i:j+1])
    #     return res

    # return sumOddLengthSubarrays(nums)

    # sample code
    # def sumEvenLengthSubarrays(self, a):
    #     l = len(a)
    #     res = sum(a)
    #     for i in range(l):
    #         for j in range(i, l, 2):
    #             res += sum(a[i:j+1])
    #     return res

    # return sumEvenLengthSubarrays(nums)

    # sample code
    # def sumSpecialArray(self, nums):
    #     l = len(nums)
    #     res = 0
    #     for i in range(l):
    #         for j in range(i, l):
    #             res += nums[i] * (j-i+1)
    #     return res

    # return sumSpecialArray(nums)

    # sample code
    # def findSpecialSum(self, nums):
    #     l = len(nums)
    #     s_sum = sum(nums)
    #     res = s_sum
    #     for i in range(l):
    #         s_sum -= nums[i]
    #        
