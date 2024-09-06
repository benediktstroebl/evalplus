```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```

The script uses dynamic programming to compute the minimum and maximum subarray sum in linear time. The minimum and maximum subarray sums are updated iteratively by adding the current element, or by considering the element as a potential new starting point for the subarray, whichever yields a smaller sum. The final result is the minimum of the two.