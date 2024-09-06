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

The function minSubArraySum takes in one argument, nums, which is the array of integers. It initializes cur_sum and min_sum respectively to 0 and the first integer in the array. It then iterates through each integer in the array, adding it to cur_sum, and resetting cur_sum to 0 if it becomes negative. It updates min_sum to the minimum value of cur_sum and min_sum at each step, and returns min_sum as the final answer.

This code effectively finds the minimum sum of any non-empty sub-array within the given array, and its logic aligns with the approach outlined in the initial prompt.