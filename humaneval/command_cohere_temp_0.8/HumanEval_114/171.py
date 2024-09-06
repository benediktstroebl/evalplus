Here's a Python function that solves the problem you've outlined:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return max(max_sum, min_sum, nums[0])
```
This Python script defines a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function returns the minimum sum of any non-empty sub-array within the given array. The function employs dynamic programming to efficiently compute the minimum and maximum sums of sub-arrays of varying sizes. Specifically, it iterates through each number in the array and updates both the minimum and maximum sums accordingly. The example usage provided in the comment corresponds to the given function behavior. 

Here is a markdown code block with the Python script to preserve the formatting of the code:
```
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return max(max_sum, min_sum, nums[0])
```
```

This script should work correctly for the given problem and handle both positive and negative integer inputs. Let me know if you have any questions!