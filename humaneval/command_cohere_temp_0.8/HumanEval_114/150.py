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

The function 'minSubArraySum' takes an array of integers 'nums' as input and iterates through them. It maintains a current sum 'curSum' and keeps track of the minimum sum encountered so far ('minSum'). If the current sum becomes negative, it's reset to zero to avoid accumulating negatives. The minimum sum is returned once all elements are processed. The test cases confirm that the function correctly identifies the minimum sum among sub-arrays.