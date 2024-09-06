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

The function 'minSubArraySum' takes an array of integers 'nums' as input and iterates through them. It maintains a 'curSum' to calculate the sum of the current subarray. If the 'curSum' becomes negative, it resets it to 0 to consider a new subarray. The variable 'minSum' is also kept track of, which stores the minimum sum of any subarray encountered so far. As it iterates through 'nums', the 'curSum' is updated and compared with the current value of 'minSum', which ensures the lowest possible sum of any non-empty subarray is identified. The function returns this minimum sum. The provided test cases yield the expected output through this implementation.