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

This script defines a function called `minSubArraySum` that takes in one argument, a list of integers called `nums`. The goal is to find the minimum sum of any non-empty sub-array within `nums`. The function achieves this by maintaining a variable `cur_sum` that tracks the sum of the current sub-array. The algorithm iterates through the elements of `nums`, adding each element to `cur_sum`. If `cur_sum` becomes negative, it's reset to 0 to account for the fact that a sub-array sum cannot be negative. Additionally, the algorithm keeps track of the minimum sum encountered thus far, initially set to the first element of nums. As it iterates through the list, this minimum is updated to reflect the smaller of the current `cur_sum` and the previously minimized sum. This allows the function to determine the minimum sum of any non-empty sub-array in the nums list, as specified by the problem statement.