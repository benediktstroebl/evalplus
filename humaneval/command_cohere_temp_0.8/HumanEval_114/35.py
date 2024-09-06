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

The function minSubArraySum takes in an array of integers called nums and iterates through them. It keeps track of the current sum of the sub-array formed so far, initialized at 0. During the traversal, if the current sum becomes negative, it resets cur_sum to 0, essentially shifting the sub-array start forward. The minimum sum is tracked continuously and is updated whenever the current sum is smaller. Finally, the minimum sum among all possible sub-arrays is returned.