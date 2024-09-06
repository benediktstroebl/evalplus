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

This script defines a function called `minSubArraySum` that takes in one argument, `nums`. The function loops through each integer in `nums`, maintaining a current sum of consecutive elements. While doing so, it keeps track of the minimum sum encountered, which might be the current sum of elements or the previous negative sum. This ensures that the minimum sub-array sum is captured accurately, including in cases where the sub-array sum turns negative. The function returns the minimum sum of any non-empty sub-array within the given array.