Here's a Python function that solves the problem you've described:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        min_sum = min(min_sum, n)
        max_sum = max(max_sum, n)
    return min(min_sum, -max_sum)
```
This Python script defines a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function finds the minimum and maximum sum of all the elements in the array, and then determines the minimum sum of any non-empty sub-array of `nums`.

To do this, it initializes both a `min_sum` and a `max_sum` to the first element in the array. It then iterates through the rest of the elements in the array, updating the minimum and maximum values as it goes. After iterating through all the elements, the function returns the minimum of the `min_sum` and the negative of the `max_sum`.

This is a deterministic way to solve the problem and obtain the minimum sub-array sum for a given array of integers.