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

This script defines a Python function called `minSubArraySum` that takes in a list of integers called `nums`. The purpose of the function is to find the minimum sum of any non-empty sub-array within the given array. To do this, it iterates through each number in the array, keeping track of both the minimum sum found so far (`min_sum`) and the maximum sum found so far (`max_sum`). 

The key insight is that if the current number is smaller than the minimum sum so far, adding it to the minimum sum will only make it smaller. Conversely, if the current number is larger than the maximum sum so far, adding it to the maximum sum will only make it larger. So, the function updates `min_sum` and `max_sum` accordingly in each iteration. Finally, the function returns the sum of these two values, which is the smallest possible sum of any sub-array in the given list. 

This approach is efficient because it solves the problem in linear time `O(n)` and uses constant extra space for the two sum variables.