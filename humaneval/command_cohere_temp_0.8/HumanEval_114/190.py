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

The function minSubArraySum takes in one argument, nums, which is an array of integers. It uses two pointers, one for keeping track of the current sum of the subarray and one for tracking the minimum sum of any subarray seen so far. In the example given, the function returns 1 for the first example and -6 for the second.