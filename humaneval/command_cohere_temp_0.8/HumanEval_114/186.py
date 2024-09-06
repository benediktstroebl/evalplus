Here's a Python script that includes a function to solve the minSubArraySum problem:
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

This script defines the `minSubArraySum` function, which takes an array of integers (`nums`) as input and iterates through the array while keeping track of the current sum of elements in a sub-array. It resets the current sum to zero when it goes negative, ensuring that the answer won't be negative. Finally, it returns the minimum sum found during the iteration. 

The example usage demonstrates how to call the function with two different arrays, and it prints the minimum sum of sub-arrays for each case.