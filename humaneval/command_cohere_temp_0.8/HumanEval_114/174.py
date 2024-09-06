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

The function minSubArraySum takes in an array of integers nums and uses a cumulative sum to keep track of the current sum of elements encountered so far. The variable min_sum is initialized to the first element of the array and is constantly updated to keep track of the minimum sum encountered so far. As the loop iterates through the array, it keeps resetting the cur_sum to 0 if it becomes negative, as any subarray with a negative sum is not considered for the minimum sum subarray. The example provided in the problem description would give a minimum sum of 1, as the subarray [1, 2, 4] has a minimum sum of 1. The final line returns min_sum, the minimum sum of any non-empty sub-array of nums.