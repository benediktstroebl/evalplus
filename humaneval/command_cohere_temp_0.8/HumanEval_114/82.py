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

The function minSubArraySum takes in one argument, nums, which is an array of integers. It uses two variables to track the current sum of the sub-array and the minimum sum of any sub-array seen so far. The function iterates through the array, keeping track of the current sum of the sub-array. If the current sum becomes negative, it starts a new sub-array sum from 0. Throughout the loop, it updates the minimum sub-array sum seen so far, min_sum, to ensure it provides the minimum value possible. Ultimately, the function returns the minimum sum of any non-empty sub-array within the inputted array.