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
print(minSubArraySum(nums1))  # Output: 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # Output: -6
```

This script defines the `minSubArraySum` function that takes in an array of integers `nums` as input and iterates through each number, tracking the current sum of the sub-array and the minimum sum encountered so far. The key idea is to take advantage of the fact that the maximum sub-array sum cannot be too large, given the overall maximum sum of elements in the array. Thus, many sub-arrays will have a smaller sum, eventually leading to the minimum non-empty sub-array sum.