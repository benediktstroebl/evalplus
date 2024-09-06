Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```
This approach uses dynamic programming to avoid redundant calculations. Initially, both the 'min_sum' and 'max_sum' variables are set to the first value in the list. The 'min_sum' is subsequently updated by summing the current value and the minimum value of either the current value or the previous 'min_sum'. The 'max_sum' is updated similarly. The function returns the minimum of the 'min_sum' and 'max_sum', guaranteeing that the lowest subarray sum is returned.