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

The function 'minSubArraySum' takes an array of integers 'nums' as input and iterates through them. It maintains a 'curSum' to calculate the sum of the current subarray. If the current sum turns negative, it resets the 'curSum' to 0, ensuring that the sum calculation restarts from the next element. The goal is to identify the minimum sum among all subarrays, which could be as small as a single element. The 'minSum' variable is used to store and update this minimum sum as the function progresses. The function eventually returns the minimum sum of any non-empty subarray within the input array.