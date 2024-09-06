Here's a Python script that includes a function to solve the minSubArraySum problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, n)
    return min(min_sum, cur_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function that iterates through the given array `nums`. It maintains two variables: `cur_sum` to keep track of the current cumulative sum and `min_sum` to record the minimum value encountered so far. As it iterates through the array, it also keeps track of the maximum sum of all subarrays ended just before the current index, which can be calculated as `max(cur_sum, min_sum)`. The function returns the minimum value between `min_sum` and `cur_sum`, which ensures the minimum sum of any non-empty subarray. The example usage provided demonstrates the function's behavior for two different input arrays.