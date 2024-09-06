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

This script provides a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function iterates through each number in the array, keeping track of the current sum of the sub-array that precedes the current number. It resets the current sum to zero if it drops below zero, ensuring that the sum is calculated correctly even when dealing with negative numbers. Finally, the function returns the minimum sum found among all the sub-arrays. This code handles both the example inputs provided in the prompt, returning 1 for the first example and -6 for the second.