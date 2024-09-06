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
This script uses a sliding window approach, summing the elements in the array one by one. If the sum goes negative, it resets to 0 to exclude the negative sum in the subarray. The minimum subarray sum will always be the smallest sum encountered during the loop, which is tracked using the `min_sum` variable.