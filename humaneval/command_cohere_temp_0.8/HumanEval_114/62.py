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

This script defines a function called `minSubArraySum` that takes in one argument, `nums`. The function iterates through the array, tracking the current sum of the sub-array and the minimum sum encountered so far. If the current sum drops below zero, it's reset to zero to avoid including a negative sum. Ultimately, the function returns the minimum sum of any non-empty sub-array within the input array. 

This will return the minimum sum of any non-empty sub-array of `nums` as specified in the example in the prompt.