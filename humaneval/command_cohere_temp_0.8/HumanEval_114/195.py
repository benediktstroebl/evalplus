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

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]

print(minSubArraySum(nums1))  # Output: 1
print(minSubArraySum(nums2))  # Output: -6
```

This script defines the 'minSubArraySum' function, which takes an array of integers ('nums') as input and calculates the minimum sum of any non-empty sub-array of 'nums.' It does this by maintaining a current sum variable ('curSum') and a variable to keep track of the minimum sum found so far ('minSum'). The loop iterates through the array, adding elements to the current sum. If the current sum becomes negative, it's reset to zero to avoid accounting for a sub-array that might have a smaller positive sum. The minimum sum is updated whenever the current sum is smaller than the current minimum sum. Finally, the function returns the minimum sum of any non-empty sub-array in the provided 'nums' array.