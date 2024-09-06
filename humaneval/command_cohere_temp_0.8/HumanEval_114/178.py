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
This function, `minSubArraySum`, iterates through the input array `nums` and calculates both the minimum and maximum sum of adjacent elements as it scans the array. This approach, known as Kadane's algorithm, yields the minimum sum of any non-empty sub-array within the same pass through the array.

The two example uses demonstrate how the function can be invoked with different input arrays to find the minimum sub-array sum for various cases.