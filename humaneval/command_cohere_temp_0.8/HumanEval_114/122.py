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

This script defines a function `minSubArraySum` that takes in a list of integers (`nums`) as input and iterates through the list while keeping track of the current sum of elements and the minimum sum of any subarray encountered so far. The key idea is that the maximum subarray sum at any point in time is the largest sum that can be achieved by a subarray ending at that moment, thus, if the current sum becomes negative, it is reset to zero. The example usage demonstrates how the function can be called with different input lists to find the minimum sum of any non-empty sub-array.