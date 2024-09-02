import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    n = len(nums)
    global_max = nums[0]
    for i in range(n):
        local_max = 0
        for j in range(i, n):
            local_max += nums[j]
            if local_max > global_max:
                global_max = local_max
    return global_max
    """
    """
    1. Initialize min number of subarray sum
    2. From each starting index, try to find the biggest 'candidate' subarray sum, 
    trashing the rest of the array
    3. Check if its increasing.   
    4. If its increasing, trim it.   
    5. Else, update min number of subarray sum 
    6. Continue until a single element remains or there are no more elements
    """

    if len(nums) == 1:
        return nums[0]
    
    # 1
    temp = nums[0]
    for i in range(1, len(nums)):
        temp = max(nums[i], temp + nums[i])
        nums[i] = temp
    
    # 2
    candidate = nums[0]
    for i in range(1, len(nums)):
        candidate = max(nums[i], candidate)
        if candidate != nums[i]:
            candidate = nums[i]
    
    # 3    
    if candidate > 0:
        return candidate
    else:
        return 0











































































































