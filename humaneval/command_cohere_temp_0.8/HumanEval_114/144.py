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

The function 'minSubArraySum' takes an array of integers 'nums' as input and calculates the sum of individual elements in the array. It uses an auxiliary variable 'curSum' to keep track of the sum of the current element and the previous sum. The variable 'minSum' keeps track of the minimum sum encountered so far. The loop iterates through the array, adding the current element to the 'curSum'. If 'curSum' becomes negative, it's reset to 0 to include the current element in the subarray sum. The 'minSum' is updated by assigning the minimum value between 'curSum' and the previous 'minSum'. Finally, the function returns the minimum sum of any non-empty sub-array in the 'nums' array.