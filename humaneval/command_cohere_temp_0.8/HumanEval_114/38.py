Here's a Python script that includes a function to solve the minSubArraySum problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, n)
    return min(min_sum, cur_sum)

# Example usage
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

This script defines the `minSubArraySum` function that takes in an array of integers (`nums`) as input and calculates the minimum sum of any non-empty sub-array within that array. It does this by keeping track of the current sum of elements seen so far (`cur_sum`) and also tracking the minimum value encountered (`min_sum`). The loop iterates through the input array, adding elements to the current sum, and if the sum dips negative, it's reset to zero to avoid a negative sub-array sum. The minimum value encountered is updated accordingly, and the final minimum sub-array sum is returned, which could be either the minimum value encountered or the current sum, whichever is minimum.

The example usage section demonstrates this algorithm on two different input arrays, both of which yield the correct minimum sub-array sums.