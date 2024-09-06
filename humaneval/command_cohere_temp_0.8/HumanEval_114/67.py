Here's a Python function that solves the problem you've outlined:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```
This approach uses a clever optimization. Notice that any subarray sum must be strictly between the smallest element and the sum of the smallest and largest elements (inclusive) in the array. Hence, we only need to iterate through the array once to compute the answer. The function returns the minimum possible sum for any non-empty subarray of `nums`.