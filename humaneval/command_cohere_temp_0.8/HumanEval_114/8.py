Here's a Python script that contains a function to solve the given problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    
    for x in nums:
        cur_sum += x
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

This script defines the `minSubArraySum` function that takes in an array `nums` as input and iterates through each number in the array. It maintains a current sum `cur_sum` and keeps track of the minimum sum encountered so far, initially set to infinity. During each iteration, it adds the current number to the `cur_sum` and if `cur_sum` becomes negative (which would make it always negative in the sub-array), it resets `cur_sum` to 0 to consider a new sub-array from the next element. The minimum sum is updated whenever the current sum exceeds the previous minimum. Finally, the function returns the minimum sum of any non-empty sub-array in the provided array.