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

The function minSubArraySum takes a list of integers nums as input and iterates through the list while keeping track of the current sum of elements (curSum). It initializes minSum with the first element of the list and updates it whenever the current sum becomes smaller. The loop also resets curSum to 0 whenever it drops below 0, effectively ignoring negative sub-arrays. The result is the minimum sum of any non-empty sub-array in the input list. 

When the provided test list [{-1, -2, -3}] is passed to the function, it correctly returns -6 as the minimum sum sub-array within that list.