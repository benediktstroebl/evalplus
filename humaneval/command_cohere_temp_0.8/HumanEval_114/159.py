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

This script defines a function called `minSubArraySum` that takes in a list of integers called `nums` as input. The purpose of the function is to find the minimum sum of any non-empty sub-array within the input list. It does so by iterating through the list, maintaining a current sum of encountered integers. If the current sum becomes negative, it resets the sum to 0, as a sub-array with a negative sum cannot be extended further. The minimum seen sum so far, tracked by the `min_sum`, is returned as the solution. The function handles both positive and negative input cases as demonstrated in the example.