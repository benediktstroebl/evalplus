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

This script provides a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The purpose of the function is to find the minimum sum of any non-empty sub-array within the given array. To achieve this, it iterates through the array, tracking the current sum of the sub-array and the minimum sum encountered so far. The loop ensures that the current sum starts anew when it drops below zero, effectively ignoring sub-arrays with negative sums. Ultimately, the function returns the minimum sum of any non-empty sub-array in the `nums` array.