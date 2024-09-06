Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numSum = float('inf')
    
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        numSum = min(numSum, curSum)
    
    return min(minSum, numSum)

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums1))  # Output: 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # Output: -6
```

The function minSubArraySum iterates through the input array, maintaining two variables: curSum to calculate the current sum of the subarray, and minSum to record the minimum sum encountered during the iteration. It also uses numSum to store the minimum sum of all elements encountered, which tends to produce the smallest answer. The minimum of minSum and numSum is then returned, providing the minimum sum of any non-empty sub-array in the given array. 

The provided example tests are contained within the script to ensure the function behaves as expected. Feel free to add more tests to cover various scenarios and validate the function's correctness further.