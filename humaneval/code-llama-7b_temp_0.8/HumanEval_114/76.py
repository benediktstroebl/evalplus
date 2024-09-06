import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    
    #define helper functions
    def helper(s):
        #if the list is empty
        if s == []:
            return 0
        
        #return minimum of the sum of all previous sums
        #to calculate the sum of the first element
        return min(helper(s[:-1]) + s[-1], s[-1])

    def left_right_sum(nums):
        #first find the sum of the first half
        #last_half = len(nums) - 1
        right_sum = 0
        left_sum = 0
        #sum the left half
        for i in range(math.ceil(len(nums)/2)):
            #for the left half, add each element to the sum
            left_sum += nums[i]
            
        #now sum the right half
        for i in range(math.floor(len(nums)/2), len(nums)):
            right_sum += nums[i]

        return min(left_sum, right_sum)

    def sum_list(nums):
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        return sum
    
    #first find the sum of the list
    list_sum = sum_list(nums)
    #find the sum of the left and right halves of the list
    left_right_sum = left_right_sum(nums)

    #return the minimum of the list_sum and the sum of the left_right halves
    return min(list_sum, left_right_sum)
