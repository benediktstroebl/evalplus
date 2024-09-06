Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, n)
    return min(min_sum, cur_sum)
```
The function minSubArraySum iterates through the input list nums and calculates the minimum sum of sub-arrays whose elements sum to zero or positive values. It keeps track of both the current sum of elements seen so far and the minimum value encountered, periodically resetting the current sum to ensure it represents the minimum sub-array sum. The function returns the minimum sub-array sum.