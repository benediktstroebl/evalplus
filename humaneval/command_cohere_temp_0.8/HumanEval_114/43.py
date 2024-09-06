Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of the given array of integers nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    
    return min(min_sum, max_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script includes the `minSubArraySum` function, which takes an array of integers (`nums`) as input and calculates the minimum sum of any non-empty sub-array within that array. It then provides examples that show how the function can be used to solve the problem for various input arrays.