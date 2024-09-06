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

This script provides a function minSubArraySum which takes in one argument, a list of integers called nums, and returns the minimum sum of any non-empty sub-array of nums. The function utilizes a sliding window approach, initially tracking the maximum sum encountered so far (min_sum) and the current sum of the window ending at the current element (cur_sum). If the current sum becomes negative, it resets to 0, as a subarray with a negative sum could be made smaller by moving the window ahead to a more positive element. The min_sum is updated whenever the current sum reaches a smaller value. Ultimately, minSubArraySum returns the minimum sum found, providing an efficient and concise solution.