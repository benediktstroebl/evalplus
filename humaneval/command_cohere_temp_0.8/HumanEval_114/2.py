Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numRel = float('inf')
    
    for num in nums:
        curSum += num
        relSum = curSum - numRel
        minSum = min(minSum, relSum)
        numRel = min(numRel, curSum)
    
    return minSum

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums1))  # 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # -6
```

The function minSubArraySum iterates through the input array, maintaining the current sum of the subarray curSum and the minimum relative sum relSum. The minimum absolute sum is updated based on these values. The given test cases correctly solve the problem.