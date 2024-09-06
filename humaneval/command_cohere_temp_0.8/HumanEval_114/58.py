Here is a Python script with a self-contained function that solves the problem:
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
```
The function 'minSubArraySum' takes an array of integers 'nums' as input and calculates the minimum sum of any subarray in the given array. It uses a dynamic programming approach to keep track of the current sum of elements and the minimum sum of individual elements encountered so far. The key insight is that the minimum sum subarray must have at least one element no less than the minimum individual element. Finally, it returns the minimum of these two values, providing the correct answer for the given problem.