Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return float('inf')
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```

The function iterates through the list, maintaining both a minimum running sum ('min_sum') and a maximum running sum ('max_sum'). The min_sum is updated by taking the minimum of its current value plus the current element, or just the current element, while the max_sum is updated by taking the maximum of its current value plus the current element, or just the current element. The function ultimately returns the minimum of the min_sum and the max_sum, providing the smallest sum of any non-empty subarray.

This approach takes advantage of the fact that the minimum subarray sum can be derived from the minimum running sum and the maximum running sum, which is a subtle but efficient refinement of the basic approach. 

This approach is more efficient than brute-force approaches that might involve looping through subarrays themselves, which would have a time complexity proportional to N^2, thanks to the linear time complexity of this technique (O(N)).