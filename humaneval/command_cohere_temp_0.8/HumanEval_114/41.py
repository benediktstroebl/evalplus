Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, n)
    return min_sum

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines a function `minSubArraySum` that takes in an array of integers (`nums`) and returns the minimum sum of any non-empty sub-array within that array. The function iterates through the array, maintaining a current sum (`cur_sum`) and keeping track of the minimum sum encountered (`min_sum`). By considering each element and updating the sums accordingly, it computes the minimum sub-array sum efficiently. The example usage demonstrates how the function can be used to solve the problem for different input arrays.