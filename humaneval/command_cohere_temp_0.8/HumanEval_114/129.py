Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes an array of integers nums as input and iterates through each number. It maintains a current sum of the subarray formed so far and keeps track of the minimum sum encountered throughout the iteration. This is achieved using the variables min_sum and cur_sum. If the current sum goes negative, it's reset to 0 to ignore the negative sum since the problem is defined for non-empty sub-arrays. Ultimately, it returns the minimum sum of any non-empty sub-array in the given nums array.