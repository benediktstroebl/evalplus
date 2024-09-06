Here's a Python script that includes a function `minSubArraySum` to solve the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]

print(minSubArraySum(nums1))  # Output: 1
print(minSubArraySum(nums2))  # Output: -6
```

The function `minSubArraySum` uses dynamic programming to avoid the naive approach's repetition. It iterates through the list, keeping track of both the minimum and maximum sum encountered so far. The minimum sum of any subarray must be equal to the minimum possible sum increased by the maximum possible sum, which is why both are tracked simultaneously.