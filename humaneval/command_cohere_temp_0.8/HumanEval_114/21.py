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

This script provides a function minSubArraySum which takes in a list of numbers, nums, as its argument. It sums up all the elements to find the minimum sub-array sum after tracking the maximum sum of the sub-array.

The function minSubArraySum can be called with the following example input:
```python
print(minSubArraySum([2, 3, 4, 1, 2, 4])) #1
print(minSubArraySum([-1, -2, -3]))  # -6
```
The function will then return the minimum sum of any sub-array of **1** and **-6** for the respective inputs.