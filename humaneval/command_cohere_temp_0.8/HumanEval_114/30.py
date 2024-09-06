Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```
This code defines a function minSubArraySum which takes in an array of integers nums. It iterates through the array, maintaining two variables, min_sum and max_sum, which represent the minimum sum of a subarray ending at the current element, and the maximum sum of a subarray ending at the current element, respectively. By updating these two variables throughout the iteration, the function finds the minimum and maximum sum of any subarray within the array, and then returns the minimum of these two values, which is the smallest sum of any non-empty subarray.