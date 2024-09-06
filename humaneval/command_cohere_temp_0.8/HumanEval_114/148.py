Here's a Python function that solves the problem you've outlined, with a markdown code block containing the Python code:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return min(max_sum, max(nums)) - min_sum
```
This function iteratively computes both the maximum sum of any subarray (using a rolling maximum sum) and the minimum sum of any subarray (using a rolling minimum sum). The overall minimum sum of any subarray is then determined by considering both the maximum subarray sum and the minimum subarray sum, ensuring the most optimal result.