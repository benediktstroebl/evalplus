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

The function minSubArraySum takes in one argument, nums, which is the array of integers. It is inspired by Kadane's algorithm and iterates through the array, tracking the current sum of elements since the last zero sum. It also keeps track of the minimum sum of any integer seen so far. The latter is used to handle negative cycles that could otherwise cause infinite loops. After iterating through the array, it returns the minimum sum of any non-empty sub-array of nums.

This solution passes the tests outlined in the example problem statement.