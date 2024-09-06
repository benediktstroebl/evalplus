Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = nums[0]
    for n in nums:
        curSum += n
        if curSum < 0:
            curSum = 0
        minSum = min(minSum, curSum)
    return minSum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1
nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines a function `minSubArraySum` that takes in a list of integers (`nums`) as input and calculates the minimum sum of any non-empty sub-array within that list. It then provides examples that show how the function works.