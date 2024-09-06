Here's a Python function that solves the problem you've outlined, along with a markdown code block showing the complete script:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)

```
This function uses dynamic programming to compute the minimum and maximum subarray sums, and then returns the minimum of these two values. 
The approach is to iterate through the array and update the minimum and maximum sum achievable after adding the current element to the sum. The final result is the minimum of the two sums.

This problem can also be approached using Kadane's algorithm (which focuses on the maximum subarray sum), and minSubArraySum behaves analogously to maxSubArraySum.