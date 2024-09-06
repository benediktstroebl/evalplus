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
This code snippet provides a function called `minSubArraySum` that takes in one argument, `nums`, which represents the array of integers. The purpose of this function is to calculate the minimum sum of any non-empty sub-array within the given array. To achieve this, the function initially tracks the current sum of elements seen so far, assuming it could be negative, and maintains the minimum sum encountered so far, initially set to the first element of the input. The function then iterates through each element in the `nums` array, adding its value to the current sum. If the current sum becomes negative, it's reset to zero to avoid cumulative sums of negative numbers. The minimum sum encountered, tracked in the `min_sum` variable, is constantly updated throughout the loop, ensuring it captures the smallest sub-array sum in the process. Finally, the function returns the minimum sum found.