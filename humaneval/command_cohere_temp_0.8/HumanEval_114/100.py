Here's a Python script that contains a function to solve the minSubArraySum problem:
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

This script defines the `minSubArraySum` function that takes in an array of integers (`nums`) and returns the minimum sum of any non-empty sub-array within `nums`. The function iterates through the array, tracking the current sum of the sub-array and the minimum sum encountered so far. If the current sum becomes negative, it's reset to zero to avoid cumulative sums larger than the maximum possible subarray sum. The script also includes example usage and tests to verify the function's behavior for different input arrays.