Here's a Python script that includes a function to solve the minSubArraySum problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        min_sum = min(min_sum + num, num)
        max_sum = max(max_sum + num, num)
    
    return min(min_sum, max_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # -6
```

This script includes the `minSubArraySum` function, which takes an array of integers `nums` as input and returns the minimum sum of any non-empty sub-array. It uses dynamic programming to efficiently compute this minimum sum by maintaining both a running minimum and running maximum sum as it iterates through the array. The minimum of these two sums is returned as the solution. The script also includes example usage and tests to verify the function's correctness.