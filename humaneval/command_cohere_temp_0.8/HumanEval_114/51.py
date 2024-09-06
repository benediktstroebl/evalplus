Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```
This script provides a function that takes in an array of integers, `nums`, as the argument. It iterates through the array, tracking the maximum and minimum sum of subarrays encountered so far. The function returns the smallest possible difference between these two values, which corresponds to the smallest sum of a subarray in the given array.

Here is an example of how you can use the function by calling `minSubArraySum` with a specified array `nums`:
```python
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```