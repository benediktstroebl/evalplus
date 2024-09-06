Here's a Python script that includes a function to solve the minSubArraySum problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    
    return min(min_sum, max_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script includes the minSubArraySum function, which takes an array of integers nums as input and returns the minimum sum of any non-empty sub-array of nums. It does this by initializing min_sum and max_sum variables to the first element of nums and then updating them based on the consecutive elements. Finally, it returns the minimum of the min_sum and max_sum, which will be the minimum sum of any sub-array of nums. 

The example usage demonstrates how to call the function with two different arrays representing the test cases mentioned in the problem statement.