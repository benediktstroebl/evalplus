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

The function minSubArraySum takes an array of integers nums as input and iterates through the array while keeping track of the current sum of elements (curSum). It also maintains a variable minSum to keep track of the minimum sum encountered so far. Each element is added to the curSum, and if the sum becomes negative, it's reset to 0 to start a new sub-array sum calculation. The minimum of curSum and minSum is updated in each iteration. Finally, the function returns the minSum, which represents the minimum sum of any non-empty sub-array in the input array. The example provided in the problem statement outputs are also included.