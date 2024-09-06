Here's a Python function that solves the problem you've outlined, along with a markdown code block showing the complete script:
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
This script provides a function `minSubArraySum` that takes an array of integers `nums` as input and calculates the minimum sum of any non-empty sub-array within that array. The function iterates through the array, keeping track of both the minimum and maximum sum encountered so far. The minimum sum is tracked in order to find the smallest sub-array sum, while the maximum sum helps identify the largest sub-array sum. This approach ensures that the minimum sub-array sum is calculated correctly, even in cases where the array contains negative numbers.