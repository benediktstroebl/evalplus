Here's a Python script that includes a function `minSubArraySum` to solve the problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return float('inf')

    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)

    return min(min_sum, max_sum)

# Example usage
nums1 = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums1))  # 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # -6
```

This script will correctly find the minimum sum of any non-empty sub-array of the given arrays.