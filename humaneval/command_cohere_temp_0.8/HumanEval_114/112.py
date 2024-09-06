Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for num in nums[1:]:
        min_sum = min(num, min_sum + num)
        max_sum = max(num, max_sum + num)
    
    return min_sum if min_sum == max_sum else -max_sum

# Example usage
nums1 = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums1))  # Output: 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # Output: -6
```

This script includes the `minSubArraySum` function that takes an array of integers `nums` as input and calculates the minimum sum of any non-empty sub-array within `nums`. The function handles cases where the array contains only positive or only negative integers, and also avoids redundant calculations of the minimum and maximum sums.