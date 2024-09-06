Here's a Python function that solves the problem you've described:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```

This function uses dynamic programming to keep track of both the minimum and maximum sum of sub-arrays ending at the current element. The minimum and maximum values are updated iteratively through the loop, and in the end, it returns the minimum of the two values, which represents the smallest sum of any non-empty sub-array.