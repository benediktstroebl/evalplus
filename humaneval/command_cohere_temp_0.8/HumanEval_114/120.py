Here's a Python function that solves the problem you've outlined, with a markdown code block containing the Python code:
```python
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    
    Example:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    >>> minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    
    return min(min_sum, max_sum)
```
This function uses dynamic programming to efficiently solve the problem. It computes both a minimum sum of successive elements and a maximum sum of successive elements as it iterates through the input array. Finally, it returns the lesser of these two sums, which is the minimum sum of any non-empty sub-array. The provided example tests demonstrate how the function behaves for different input arrays.