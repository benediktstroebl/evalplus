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
    return min(min_sum, cur_sum)
```
The function 'minSubArraySum' takes an array of integers 'nums' as input and calculates the minimum sum of any subarray within that array. It does so by maintaining two variables: 'cur_sum' tracks the sum of elements seen so far, and 'min_sum' keeps track of the minimum value encountered thus far. The loop iterates through the input array, adding elements to the 'cur_sum'. If 'cur_sum' falls below zero, it's reset to zero, ensuring that the cumulative sum remains valid. The 'min_sum' is updated at each iteration to retain the minimum value seen so far. Finally, the function returns the minimum of 'min_sum' and 'cur_sum', which guarantees the smallest possible sum of any non-empty subarray in 'nums'.