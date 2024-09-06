Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in an array of integers nums and uses Kadane's algorithm to iteratively calculate the current sum of the subarray and the minimum sum encountered so far, ultimately returning the minimum sum of any non-empty sub-array in nums. This algorithm is efficient and uses only a single pass through the input array.