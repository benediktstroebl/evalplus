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

The function minSubArraySum takes in one argument, nums, which is an array of integers, and returns the minimum sum of any non-empty sub-array of nums. The function initializes cur_sum to 0 and min_sum to the first element of the array. It then iterates over each element in the array, adding it to cur_sum. If cur_sum goes negative, it's reset to 0 to account for the fact that a subarray sum cannot be negative. min_sum is updated by assigning the minimum of its current value and cur_sum at each step. Finally, the function returns min_sum, which represents the minimum sum of any non-empty sub-array of the input array.