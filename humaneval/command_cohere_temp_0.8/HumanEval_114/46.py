Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    """
    Find the minimum sum of any non-empty sub-array of nums.
    """
    if not nums:
        return 0  # Empty array, sum is 0
    min_sum = nums[0]  # Initialize min_sum with the first element
    for i in range(1, len(nums)):
        # Calculate the sum of the current element and the minimum sum so far
        cur_sum = nums[i] + min_subarray_sum
        # Update min_sum if the current element contributes a smaller sum
        if cur_sum < min_sum:
            min_sum = cur_sum
    return min_sum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function, which iterates through the array and keeps track of the minimum sum of any sub-array seen so far. The example usage demonstrates how to use this function to solve the problem.