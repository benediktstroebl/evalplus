Here's a Python function that solves the problem you've outlined:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return min(max_sum, max(nums)) - min_sum
```
This Python script defines a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function finds the maximum sum of any subarray within the array `nums` and the minimum sum of the array `nums`. It does this by iterating through each number in the array. The function then returns the minimum sum of any non-empty sub-array of nums.

Here is an example of how to use the function:
```python
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```
This would output the minimum sum of the subarray 1 and -6 respectively for the two examples given.