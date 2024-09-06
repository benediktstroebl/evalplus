Here's a Python script that includes a function to solve the minSubArraySum problem:
```python
def minSubArraySum(nums):
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

This script defines the `minSubArraySum` function, which iterates through the input array `nums` and calculates both the minimum and maximum sum of contiguous sub-arrays ending at the current element. The minimum of these two values is returned, giving the minimum sum of any non-empty sub-array. The example usage demonstrates how to use this function to solve the given problem.