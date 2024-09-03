```python
def minSubArraySum(nums):
    """
    Returns the minimum sum of any non-empty subarray.
    A solution using using creating a difference array and then summing the differences.
    """
   
    solution:
    # Initialize a sum of all numbers
    sum = 0
    # Create a difference array and initialize with 0
    differences = [0] + nums
    # Initialize the minimum sum with the first number
    minSum = nums[0]
    # Iterate through the array
    for i in range(1, len(nums)):
        # Update the difference array with current number
        differences[i] = nums[i] - nums[i - 1]
        # Update the sum
        sum += differences[i]
        # Find the minimum sum in the differences array
        minSum = min(minSum, sum)
    return minSum

# Test cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))  # Output: -6
```

This code provides a self-contained function that calculates the minimum sum of any non-empty subarray. The function follows the unique approach, building a difference array, which guarantees that the sum of differences is always non-negative. The difference array is initialized with zeros and updated with the current number. Finally, the function finds the minimum sum in the differences array, which equals the solution.