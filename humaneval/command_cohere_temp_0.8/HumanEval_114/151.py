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

This code defines a function `minSubArraySum` that takes in a list of integers `nums` as its input. It initializes `min_sum` to infinity to account for the possibility of negative sums, and then iterates through the list, maintaining a current sum `cur_sum` of the subarray. If `cur_sum` dips negative, it's reset to 0 to start a new subarray sum calculation. The `min_sum` is always updated from `cur_sum` when necessary, ultimately returning the smallest subarray sum found.