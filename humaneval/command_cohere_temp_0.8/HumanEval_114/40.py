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

This script provides a function called `minSubArraySum` that takes in one argument, a list of integers called `nums`. The purpose of the function is to calculate the minimum sum of any non-empty sub-array within the given list of integers. The function uses an optimized approach using dynamic programming. It maintains two variables: `cur_sum` to track the sum of the current subarray, and `min_sum` to keep track of the minimum sum encountered so far. The function iterates through the list of integers, adding each value to the `cur_sum`. If the sum becomes negative, it resets `cur_sum` to 0, since any subarray that begins with a negative sum will only decrease the total sum, hence ignoring it and moving to the next subarray is the optimal strategy. The `min_sum` variable is updated throughout the loop, keeping track of the minimum sum encountered so far, with the initial value being the first element in the nums array. At the end of the loop, the function returns the min_sum, which is the minimum sum of any non-empty sub-array within the given nums.

This script addresses the problem statement given in the previous message and provides a solution while adhering to the specified coding conventions. It can be executed directly on any Python environment that supports Markdown code blocks, such as the Cohere Playground.