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
    return min_sum
```

This script defines a function called `minSubArraySum` that takes in one argument, `nums`. The function iterates through the array, tracking the current sum of the sub-array and the minimum value encountered so far. In this way, it determines the minimum sum of any non-empty sub-array of `nums`. This solution is efficient in terms of time and space complexity, as it uses only a single pass through the input array.