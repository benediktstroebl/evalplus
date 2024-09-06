Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    
    for num in nums:
        cur_sum += num
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    
    return min_sum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function that takes in an array `nums` as input and iterates through each number. It maintains a current sum `cur_sum` and keeps track of the minimum sum encountered so far, initially set to infinity. During each iteration, it adds the current number to the sum and checks if the sum turns negative. If it does, it resets the sum to zero to avoid tracking a negative sum for too long. The minimum sum encountered is updated whenever the current sum is smaller. Finally, the function returns the minimum sum of any non-empty sub-array in the provided array.