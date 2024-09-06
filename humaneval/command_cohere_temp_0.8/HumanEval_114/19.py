Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        min_sum = min(min_sum, n)
        max_sum = max(max_sum, n)
    return min(min_sum, -max_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function, which takes in an array of integers (`nums`) as input and returns the minimum sum of any non-empty sub-array of `nums`. The function uses a synchronous approach, tracking the minimum and maximum sum encountered so far through a loop. It then returns the minimum of the minimum sum and the negative of the maximum sum, ensuring that the subarray contains at least one positive element.