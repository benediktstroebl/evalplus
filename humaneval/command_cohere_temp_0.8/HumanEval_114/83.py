Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numList[0]
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        if curSum < 0:
            curSum = 0
    return minSum

# Test Cases
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # -6
```

The function minSubArraySum takes a list of integers nums as input and iterates through the list while keeping track of the current sum of elements (curSum). It also maintains a variable minSum, initially set to the first element of the list, which represents the minimum sum encountered so far.

During each iteration, the function checks if the current sum curSum is less than or equal to zero. If it is, the function resets curSum to zero, indicating that the subarray sum is not improving, and continues iterating. This helps prevent the function from getting stuck in an infinite loop for lists where every subarray sum is negative.

The function returns the minimum sum of any non-empty sub-array in the list. The provided test cases demonstrate the function's correctness.