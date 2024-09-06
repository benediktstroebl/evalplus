Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in an array of integers nums and uses an ingenious technique to optimize the solution. It keeps track of the current sum of the sub-array while iterating through the array. If the current sum becomes negative, it resets the sum to zero, effectively "resetting" the sub-array. This is a crucial technique in optimizing the solution.

By keeping track of the minimum sum encountered among these sub-arrays, it ultimately finds the minimum sum of any non-empty sub-array in the provided array. This method of "resetting" sub-arrays is often referred to as the KKT condition technique and is a common optimization used in dynamic programming-based solutions.