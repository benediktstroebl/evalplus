Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum if max_sum - min_sum else max_sum
```

The function uses both a minimum and maximum sub-array sum, initially set to the first element in the array, to efficiently compute the solution. It iterates through the array, updating the minimum and maximum sum accordingly. The final answer is the minimum sum plus the maximum sum, minus their difference, or just the maximum sum if they are equal, denoting an array with all positive or negative elements.

This approach's time complexity is `O(n)`, where `n` is the number of elements in the array, as it uses only a single pass. The space complexity is `O(1)`, as it utilizes a constant amount of extra space.