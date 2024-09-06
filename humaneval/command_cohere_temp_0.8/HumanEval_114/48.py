Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for num in nums:
        cur_sum += num
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

This script provides the function 'minSubArraySum' that takes in one parameter, a list of 'nums' and returns the minimum sum of any sub-array within 'nums'. The script employs a sliding window approach, iterating through the list and tracking the current sum of the array. After each iteration, it checks if the current sum is less than zero, resetting the sum to zero if it is, to avoid negative sums. Simultaneously, it keeps track of the minimum sum encountered during the iterations, using the 'min' function to compare the current sum with the previous 'min_sum'. This ensures that the function returns the minimum possible sum of a sub-array within the input list.