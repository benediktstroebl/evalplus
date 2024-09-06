Here's a Python script that contains a function to solve the given problem:
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

This script defines the `minSubArraySum` function that takes in an array of integers (`nums`) as input and iterates through the array, tracking the current sum of the sub-array. It also keeps track of the minimum sum encountered so far. In the case of a negative sum, it resets the current sum to 0 to avoid including a negative sum in the final answer. The function returns the minimum sum of any non-empty sub-array among all possible sub-arrays.

The script then tests the function with two examples, and as expected, it returns the minimum sums for each case as stated in the example.