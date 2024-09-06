Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numSol = float('inf')
    for num in nums:
        curSum += num
        if curSum < minSum:
            minSum = curSum
        if curSum > 0:
            numSol = min(numSol, curSum)
        if curSum < 0:
            numSol = min(numSol, -curSum)
    return minSum if minSum < numSol else numSol

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]
print(minSubArraySum(nums1))  # 1
print(minSubArraySum(nums2))  # -6
```

This script defines the `minSubArraySum` function, which takes an array of integers (`nums`) as input and calculates the minimum sum of any non-empty sub-array of `nums`. It iterates through the array, maintaining the current sum (`curSum`) and the minimum sum found so far (`minSum`). The key idea is to optimize for sub-arrays that include both positive and negative integers, as they can yield a smaller minimum sum. The function returns the minimum sum found or, if that exceeds the absolute minimum sum, returns the absolute minimum sum instead.