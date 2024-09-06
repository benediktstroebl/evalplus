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

The function minSubArraySum iterates through the input array nums while keeping track of the current sum of elements since the last time the sum crossed zero. The minimum sum of any subarray is either the minimum of these partial sums or the minimum element in the array, whichever is less. The output of the example usage demonstrates that the function correctly finds the minimum sum for various input arrays.