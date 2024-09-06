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

The function minSubArraySum takes an array of integers nums as input and iterates through the array while keeping track of the current sum of elements in a sub-array. If the current sum becomes negative, it starts a new sub-array by resetting the curSum to 0. The minimum sum of any non-empty sub-array is the smallest of the overall sum of elements in that sub-array (`curSum`) and the minimum sum encountered so far (`minSum`). The function returns the final minimum sum of any non-empty sub-array.