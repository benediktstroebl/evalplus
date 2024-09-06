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
    return min_sum
```

This script provides a function minSubArraySum which takes in one argument, a list of integers called nums, and returns the minimum sum of any non-empty sub-array within nums. The script employs a sliding window approach, initially tracking the minimum sub-array sum encompassing all elements up to the most recent one ('min_sum'). The algorithm iterates through the list, adding each element to the current sum ('cur_sum') while tracking the minimum relevant sum so far. If the current sum drops below zero, it resets to zero, ensuring a fresh start with the next element. Finally, the algorithm returns the minimum sub-array sum. 

The `minSubArraySum` function can be tested by calling it with a list of integers and comparing the returned result to the expected outcome.