Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```
This script defines a function called `minSubArraySum` that takes in one argument, `nums`. The function iterates through the list, maintaining two variables, `min_sum` and `max_sum`, which represent the minimum and maximum sum of contiguous sub-arrays encountered so far. During each iteration, the function updates these variables by computing the minimum and maximum sum achievable with the current element `n`, either as a standalone sum or combined with the previous `min_sum` or `max_sum`. Ultimately, the function returns the sum of these two variables, effectively finding the lowest possible sub-array sum in the process.