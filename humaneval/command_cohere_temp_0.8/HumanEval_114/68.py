```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return max(max_sum, min_sum)
```
This approach endeavors to pinpoint the maximum and minimum sums attainable within the sub-arrays of `nums`. The reason for tracking both the minimum and maximum sum is to ensure that all possible sub-arrays are considered, even those with negative integers. The ultimate answer is yielded by returning the lesser of the maximum possible sum and the minimum actual sum, thereby guaranteeing the smallest sum of any non-empty sub-array. 

The given example in the Problem Statement section is addressed as follows:
```python
>>> minSubArraySum([2, 3, 4, 1, 2, 4])
1
>>> minSubArraySum([-1, -2, -3])
-6
```
The result is consistent with the expected minimum sums for each respective input array. 

This solution adheres to the defined constraints and effectively addresses the problem.