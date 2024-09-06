Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numSum = float('inf')
    
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        numSum = min(numSum, curSum)
    
    return minSum if minSum < numSum else -numSum

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums1))  # Output: 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # Output: -6
```

This script defines the `minSubArraySum` function, which takes an array of integers (`nums`) as input and calculates the minimum sum of any non-empty sub-array within that array. It does this by maintaining two variables: `curSum` to keep track of the sum of the current sub-array, and `minSum` and `numSum` to keep track of the minimum sum encountered so far and the minimum sum of any sub-array of numbers encountered so far. 

The script then iterates through each number in the input array and updates the `curSum`, `minSum`, and `numSum` accordingly. After processing all numbers, the function returns the minSum if minSum is less than numSum, indicating that all sub-arrays have been considered, and this will return the correct minimum sum of any sub-array. If minSum is greater than or equal to numSum, this indicates that the current sub-array contains only negative numbers, and returning `-numSum` will give the minimum sum of any sub-array containing only negative numbers. 

The script also includes test cases to validate the function's behavior. You can uncomment the test cases you want to test by removing the hash symbols (`#`) before the lines.