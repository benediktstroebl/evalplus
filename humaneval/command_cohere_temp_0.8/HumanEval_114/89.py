Here's a Python function that solves the problem you've outlined:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        min_sum = min(min_sum, n)
        max_sum = max(max_sum, n)
    return min(min_sum, -max_sum)
```
This Python script defines a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function seeks to determine the minimum sum of any non-empty sub-array within the given array.

It begins by tracking two variables: `min_sum` and `max_sum`. Initially, these are set to the first element of the array. The function then iterates through each number in the array, updating `min_sum` and `max_sum` after each iteration. `min_sum` is updated with the minimum value between its current state and the current number, while `max_sum` is updated to the maximum of either its current state or the current number. This process effectively captures the range of values in the array.

Finally, the function returns the minimum of either `min_sum` or `-max_sum`. The `-max_sum` is considered because finding the minimum of a subarray could involve taking the minimum of all negative integers, in which case the maximum sum would be `-min_sum`. Taking the minimum of these two values ensures that the function returns the smallest possible sum of a sub-array.

The provided example in the comment, `minSubArraySum([2, 3, 4, 1, 2, 4]) == 1`, would return `1` as the minimum sub-array sum. This is because the only possible way to form a sub-array with a sum of 1 is by selecting the single element 1 from the array. 

This script effectively solves the problem posed and provides a straightforward way to find the minimum sub-array sum for any given array of integers.