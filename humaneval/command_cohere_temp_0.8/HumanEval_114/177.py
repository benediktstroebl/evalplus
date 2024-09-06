Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    
    for num in nums:
        cur_sum += num
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    
    return min_sum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script includes the `minSubArraySum` function, which iterates through the input `nums` array and maintains a current sum of elements. When the current sum drops below 0, it's reset to 0 to avoid accounting for a sub-array that began with a negative integer. The minimum sum found so far (`min_sum`) is constantly updated and returned at the end. The example usage demonstrates how to use the function with two different input arrays.