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

The function minSubArraySum takes in one argument, nums, which is an array of integers. It initializes cur_sum and min_sum to the first element of nums and iterates through the rest of the elements in the array. If the current sum of elements in the array becomes negative, it resets cur_sum to 0 to start a new subarray sum from the next element. It keeps track of the minimum subarray sum seen so far, min_sum, and returns the final minimum subarray sum after processing all elements.