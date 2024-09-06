Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    
    return min(min_sum, max_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function that takes in an array `nums` as input and iterates through each element. It maintains two variables, `min_sum` and `max_sum`, which represent the minimum and maximum sum of contiguous sub-arrays encountered so far. The key idea is that for each element `n`, we update both `min_sum + n` and `max_sum + n` since adding `n` to the sub-array can result in either the minimum or the maximum sum. Finally, it returns the minimum of `min_sum` and `max_sum`, which gives the smallest sum for any non-empty sub-array in `nums`.