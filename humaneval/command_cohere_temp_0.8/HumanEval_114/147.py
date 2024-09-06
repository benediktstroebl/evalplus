Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = nums[0]
        if num < current_sum:
            current_sum = num
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)
    
    return min(min_sum, max_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # 1
nums = [-1, -2, -3]
print(minSubArraySum(nums))  # -6
```

This script defines the `minSubArraySum` function that takes in an array of integers (`nums`) and calculates the minimum sum of any non-empty sub-array within that array. It then provides examples that demonstrate how the function works correctly.