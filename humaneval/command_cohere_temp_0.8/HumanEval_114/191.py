Here's a Python function that solves the problem you've outlined, with a markdown code block containing the Python code:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return min(max_sum, max(nums)) - min_sum
```

The function 'minSubArraySum' takes a list of integers called 'nums' as input. It operates on two variables 'min_sum' and 'max_sum'. 'min_sum' tracks the minimum sum of any subarray seen so far, while 'max_sum' tracks the maximum sum of any subarray seen so far. The algorithm iterates through the input list 'nums' and updates 'max_sum' by considering two cases for each element: the current element itself and the current element added to the previous 'max_sum'. This way, 'max_sum' captures the maximum sum of any subarray, regardless of whether the subarray grows or shrinks. 'min_sum' is updated similarly to track the minimum sum of any subarray. Finally, the function returns the minimum possible difference between the maximum and minimum subarray sums, which is the answer to the problem.