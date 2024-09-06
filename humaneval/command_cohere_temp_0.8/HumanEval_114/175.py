Here is a Python script with a self-contained functionDr that solves the problem using a sliding window approach:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```

The `minSubArraySum` function takes an array of integers `nums` as input and uses a sliding window approach to keep track of both the minimum and maximum sum of sub-arrays. The minimum is tracked by iteratively updating it to be the smaller of the current element and the sum of the current element and the previously recorded minimum. The maximum is tracked similarly. The answer is determined to be the sum of the recorded minimum and maximum sums, ensuring that the sub-array with the minimum sum will always have a sum of at least the minimum sum and no more than the maximum sum. This approach is efficient and deterministic, with a time complexity of `O(n)`, where `n` is the length of the input array.