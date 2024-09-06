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

The function minSubArraySum takes in one argument, nums, which is the array of integers. It is inspired by Kadane's algorithm and iterates through the array, tracking the current sum of the subarray formed so far. If the current sum becomes negative, it resets the current sum to 0, essentially discarding that subarray. It also keeps track of the smallest value encountered, which could potentially be the minimum sum of any non-empty subarray. Ultimately, the function returns the minimum possible sum of any subarray.

To ensure that the function correctly identifies the minimum subarray sum, it keeps track of the current sum and resets it to zero if it becomes negative. This mechanism allows the function to consider subarrays both in their entirety and partially, depending on their impact on the overall sum. In the end, it returns the minimum sum achievable using all elements of the array.