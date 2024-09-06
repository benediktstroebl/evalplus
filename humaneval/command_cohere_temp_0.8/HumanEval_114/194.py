Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in an array of integers nums and finds the minimum sum of any sub-array within *nums*. It does so by maintaining a cur_sum variable, which is the sum of seen elements so far, and a min_sum variable, which is the minimum sum encountered so far. As it iterates through *nums*, it keeps updating *cur_sum* and checks if it dips below zero, in which case it resets it to zero to ignore the current sub-array. At the same time, it keeps tracking the minimum sum seen so far with *min_sum*. This way, the function returns the minimum sum of any non-empty sub-array in *nums*.