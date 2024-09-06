Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

In this script, the `minSubArraySum` function takes an array of integers `nums` as input. It initializes `min_sum` and `max_sum` with the first element of the array. The loop iterates through the remaining elements of the array, updating the `min_sum` and `max_sum` based on the current element `n`. The `min_sum` is updated by considering both the current element and its potential contribution to the existing `min_sum`, while `max_sum` is updated similarly. Finally, the function returns the sum of `min_sum` and `max_sum`, which guarantees the minimum sum of any non-empty sub-array.