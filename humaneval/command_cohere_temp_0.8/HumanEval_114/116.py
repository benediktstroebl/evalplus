Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```
This approach is intuitive and has a time complexity of O(n), where n is the length of the input array `nums`. It achieves this by iteratively updating both a minimum running sum `min_sum` and a maximum running sum `max_sum` as it iterates through the input array. This ensures that the minimum and maximum sum of all subarrays of length 1 or greater are recorded, which allows us to easily compute the minimum sum of any non-empty subarray.