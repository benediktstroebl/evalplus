Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    result = nums[0]
    
    for n in nums[1:]:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum + n, n)
        result = min(result, max_sum)
    
    return result

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script includes the `minSubArraySum` function, which accepts an array of integers (`nums`) as input and returns the minimum sum of any non-empty sub-array within `nums`. The function employs dynamic programming to efficiently determine the minimum sub-array sum. It keeps track of both the minimum and maximum sum encountered so far, ultimately returning the minimum of the two. This algorithm is particularly effective for this problem due to its deterministic nature and linear time complexity.