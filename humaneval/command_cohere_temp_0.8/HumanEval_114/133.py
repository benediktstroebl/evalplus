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

This script provides a function minSubArraySum which takes in an array of integers nums and returns the minimum sum of any non-empty sub-array of nums. The function employs a sliding window approach, iterating through each element of the array and calculating the current sum of elements in that window. If the sum goes negative, it resets the sum to 0, essentially moving the window to start from the next element. Throughout this process, it keeps track of the minimum sum encountered, which is eventually returned.