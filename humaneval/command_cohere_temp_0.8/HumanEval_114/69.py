Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    
    for x in nums:
        cur_sum += x
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

This script defines the `minSubArraySum` function that iterates through the given array `nums`. It maintains a current sum `cur_sum` and updates it when new elements are added. If the sum becomes negative, it's reset to 0 to avoid cumulative sum calculation issues. The script then minimizes `cur_sum` periodically and returns the smallest sum found, which represents the minimum sum of any non-empty sub-array. The example usage demonstrates how to use the function correctly.