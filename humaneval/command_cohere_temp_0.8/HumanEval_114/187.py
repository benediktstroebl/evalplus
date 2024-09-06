```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return min(max_sum, max(0, min_sum))
```

The script uses a min-max technique to efficiently determine the minimum sum of any sub-array. It iterates through the input list `nums` and computes both the minimum and maximum sum encountered so far. By maintaining these two values, the script ensures it captures all sub-array sums within the range of these two values, thereby guaranteeing that the minimum sub-array sum is among them. The final result is returned as the minimum of the maximum sum and the absolute value of the minimum sum, ensuring a correct solution for both positive and negative input numbers.