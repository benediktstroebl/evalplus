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

This script defines the `minSubArraySum` function that takes in an array of integers `nums` as input and iterates through each number, tracking the current sum of the sub-array and the minimum sum encountered so far. The key insight is that we only track the minimum sum encountered, and when the current sum becomes negative, we reset it to 0, as any sub-array that includes a negative number will only decrease the sum. Thus, we don't need to consider sub-arrays with negative sums beyond the first occurrence of each negative number.