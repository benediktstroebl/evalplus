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
This code defines a function minSubArraySum which takes in one parameter, a list of integers called nums. It aims to find the minimum sum of any non-empty sub-array within the given array. Initially, the function computes the current sum of the sub-array starting from index 0, updating it as it iterates through the array, checking if the current sum becomes negative (indicating a new sub-array needs to be started). The function keeps track of the minimum sum encountered during this process, ultimately returning the minimum sum of any non-empty sub-array.