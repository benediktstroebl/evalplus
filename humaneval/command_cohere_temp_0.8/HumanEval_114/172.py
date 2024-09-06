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

The function minSubArraySum takes in an array of integers nums and iterates through them, tracking the current sum of the sub-array. If the current sum goes negative, it resets the sum to 0, essentially starting a new sub-array sum calculation. The minimum sum found so far is kept track of in the variable min_sum, and the final minimum sum of any non-empty sub-array is returned.