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

The function minSubArraySum takes in one argument, nums, which is an array of integers. It uses two variables to track the current sum of the sub-array, `cur_sum`, and the minimum sum of any encountered value in the array `min_sum`. The function adds the integer n to the current sum of the subarray, `cur_sum` while iterating through the numbers. If the sum becomes negative, it resets it to 0, to account for a better answer further in the array. It also updates the `min_sum` if the current integer in the array provides a smaller minimum. Ultimately, the function returns the minimum possible sum of a sub-array in the given array.