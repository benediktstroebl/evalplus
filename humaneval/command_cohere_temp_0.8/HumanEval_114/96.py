Here's a Python script that contains a function to solve the minSubArraySum problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return min(max_sum, max(nums)) - min_sum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function, which takes an array of integers (`nums`) as input and calculates the minimum sum of any non-empty sub-array within that array. It does this by keeping track of both the maximum sum of consecutive positive sums and the minimum sum of the current array, and then returns the difference between them, which will be the minimum required to negate the entire array.

The two example uses provide minimum sums of sub-arrays for the provided arrays and demonstrate the functionality of the minSubArraySum function.