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

nums = [-1, -2, -3]
print(minSubArraySum(nums))
```

The function minSubArraySum takes a list of integers nums as input and iterates through the list while keeping track of the current sum of elements since the last time the sum was zero or less than zero. It maintains two variables: minSum, which stores the minimum sum of any subarray found so far, and curSum, which represents the sum of elements in the current subarray. The example provided in the description of the problem would print `-6` as the output.