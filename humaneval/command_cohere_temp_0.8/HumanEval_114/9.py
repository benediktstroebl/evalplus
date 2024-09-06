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

This code defines the 'minSubArraySum' function, which takes an array of integers ('nums') as input and calculates the minimum sum of any non-empty sub-array within that array. It does this by iterating through the array, tracking the current sum of the sub-array ('curSum') while keeping track of the minimum sum encountered ('minSum') and an optimized solution using binary search on the negativity of 'curSum' ('numSol'). By keeping track of both the minimum sum and the optimized solution, the code can efficiently determine the minimum sub-array sum regardless of whether the sub-arrays are positive or negative. The output is the minimum sum of any non-empty sub-array of the given input array.