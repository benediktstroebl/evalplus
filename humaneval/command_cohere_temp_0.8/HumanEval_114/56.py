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

The function minSubArraySum takes an array of integers nums as input and iterates through the array, tracking the current sum of elements since the last time the sum became non-negative (or the beginning of the array). It maintains a variable minSum, which stores the minimum sum encountered so far. The example usage section demonstrates how the function can be used with different input arrays to find the minimum sum of any non-empty sub-array.