Here's a Python function that solves the problem you've described:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```

This script provides a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The purpose of this function is to calculate the minimum sum of any non-empty sub-array within the given array. To accomplish this, it keeps track of both the minimum and maximum sum encountered so far, using the initial element of the array as both the initial minimum and maximum sum. Then, it iterates through the remainder of the array, updating the minimum sum by either taking the smaller of the current element or the sum of the current element and the minimum, and updates the maximum sum by either taking the larger of the current element or the sum of the current element and the maximum. The function returns the sum of the minimum and maximum sums, providing an optimal result for the given query.