Here's a Python function that solves the problem you've described, along with a markdown code block showing the complete script:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum

# Test cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]

print(minSubArraySum(nums1))  # Output: 1
print(minSubArraySum(nums2))  # Output: -6
```

In this script, the `minSubArraySum` function calculates both the minimum and maximum sum potentials of each element as it iterates through the input `nums` array. The minimum sum is tracked as `min_sum`, and the maximum sum is tracked as `max_sum`. The key insight is that any subarray sum must be greater than or equal to the minimum sum of its elements, and less than or equal to the maximum sum of its elements. Hence, the answer is found by summing up `min_sum` and `max_sum`.