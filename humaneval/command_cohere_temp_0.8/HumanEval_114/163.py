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

This script defines a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function iterates through the array, maintaining a current sum of elements seen so far (`cur_sum`). It also keeps track of the minimum sum encountered (`min_sum`). The key idea is to reset the current sum to zero whenever it falls below zero, effectively ignoring all previous negative sums. This allows the function to correctly handle negative elements within the array. The function returns the minimum sum of any non-empty sub-array within the given array.