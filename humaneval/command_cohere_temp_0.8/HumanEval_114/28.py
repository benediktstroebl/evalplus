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

The function minSubArraySum takes in one argument, nums, which is an array of integers. It then iterates through the array, maintaining a current sum of the sub-array between the current element and the start of the array. If the current sum goes negative, it resets the current sum to 0, essentially "resetting" the sub-array counter. It then updates the min_sum to the minimum value between the current sum and the min_sum recorded so far. Ultimately, the min_sum recorded will be the minimum sum of any non-empty sub-array within the input array.

This approach takes advantage of the fact that the minimum sub-array sum can only be negative, thus whenever the sum crosses 0, it can only get more negative, so we can reset the sub-array sum to 0, and use this to minimize the sub-array sum. It is efficient in terms of time and space complexity, as it uses only a single pass through the input array and does not require any additional space.