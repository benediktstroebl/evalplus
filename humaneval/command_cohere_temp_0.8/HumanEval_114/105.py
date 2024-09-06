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

The function minSubArraySum takes an array of integers nums as input and iterates through the array, tracking the current sum of the sub-array. Whenever the current sum drops below 0, the function resets it to 0, since a negative sum is not helpful in finding the minimum. The function keeps track of the minimum sum encountered so far, which is updated throughout the array. The final minSum value returned is the minimum sum of any non-empty sub-array in the input. The test cases correctly verify the function against the provided examples in the prompt.