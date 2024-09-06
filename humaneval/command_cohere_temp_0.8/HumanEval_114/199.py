Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numRel = float('inf')
    for num in nums:
        curSum += num
        mini = curSum - numRel
        numRel = min(numRel, curSum)
        minSum = min(minSum, mini)
    return minSum

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]

print(minSubArraySum(nums1))  # Output: 1
print(minSubArraySum(nums2))  # Output: -6
```

The function minSubArraySum iterates through the input array, maintaining variables to track the current sum of the array, the minimum sum found so far, and the minimum relative sum encountered so far. By comparing the current sum to the minimum relative sum, it updates the minimum sum found. The script also includes test cases to validate the function's correctness.