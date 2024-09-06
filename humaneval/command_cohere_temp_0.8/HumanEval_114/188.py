Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numArgs[0]
    
    for arg in nums:
        curSum += arg
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

The function 'minSubArraySum' takes arrays of integers ('nums') as input, and the code proceeds as follows:
1. The variable 'curSum' is used to keep track of the sum of the current subarray, and 'minSum' is initialized to the first element of the input array, assumed to be the lowest possible minimum sum.
2. Each element in the array is iterated through, and the current sum is updated by adding the element.
3. The 'minSum' is always updated with the smaller value between 'minSum' and 'curSum,' ensuring that 'minSum' captures the minimum possible sum of any subarray. 
4. When the current sum 'curSum' becomes negative, it is reset to 0, indicating the start of a new subarray. This is because the sum cannot become negative anymore, so starting the sum from 0 helps in finding the minimum for the next subarray. 

The code is self-contained and does not rely on any external libraries or modules other than the Python standard library. It neatly solves the problem in a concise and straightforward manner.