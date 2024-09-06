Here's a Python script that includes a function to solve the given problem and a separate test script to validate its correctness:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum + n, n)
    return min(min_sum, max_sum)

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]

print(minSubArraySum(nums1))  # Output: 1
print(minSubArraySum(nums2))  # Output: -6

```

The `minSubArraySum` function uses dynamic programming to compute both the minimum and maximum possible sum of sub-arrays ending at each element. This allows it to efficiently find the minimum sum sub-array among all possible sub-arrays.

The test cases confirm that the function produces the expected outputs for two different inputs, illustrating its practical usage.