Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```
This script provides a function that takes in a list of integers, `nums`, as the input. It iterates through the list, tracking the current sum of the sub-array. If the sum turns negative, it resets the sum to 0, effectively "shifting" the threshold of considering a sub-array's sum to be negative. Throughout the iteration, it keeps track of the minimum sum encountered, which is updated as a new minimum whenever a positive overall sum is found. Ultimately, the function returns the minimum sum of any non-empty sub-array in the given input list.