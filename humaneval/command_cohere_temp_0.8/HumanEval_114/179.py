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

The function minSubArraySum takes in an array of integers called nums and calculates the minimum sum of any non-empty sub-array within that array. It achieves this by maintaining a cur_sum variable, which tracks the sum of elements seen so far. When cur_sum dips below zero, it's reset to 0, indicating a new sub-array. The function iterates through the array, keeping track of the minimum sum encountered, stored in min_sum. This approach ensures that min_sum captures the smallest sum of any sub-array, including those with negative elements.