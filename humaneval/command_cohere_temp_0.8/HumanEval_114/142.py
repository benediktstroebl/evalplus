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

This function uses dynamic programming to keep track of both the minimum and maximum sum possibilities as it iterates through the array. This allows it to accurately compute the minimum sum of any non-empty sub-array.