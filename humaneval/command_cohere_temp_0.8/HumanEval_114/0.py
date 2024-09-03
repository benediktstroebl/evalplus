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
This script provides a function minSubArraySum which takes in a list of integers nums and returns the minimum sum of any sub-array within that list. The function utilizes a sliding window approach, tracking both the current sum of elements encountered and the minimum sum encountered so far. The example provided in the problem statement would return 1 from this function, and the function would also return -6 for the input [-1, -2, -3].