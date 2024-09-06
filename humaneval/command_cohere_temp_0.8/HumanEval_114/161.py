```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```
This code defines a function minSubArraySum which takes in a list of numbers, nums, as input. The function first initializes two variables, min_sum and max_sum, with the first value in the list, nums[0]. Then, it iterates through the remaining numbers in the list, updating min_sum and max_sum accordingly. In each iteration, the function computes the minimum sum of all subarrays ending at that point by taking the smaller of the current number n or the sum of n and min_sum. It similarly computes the maximum sum of all subarrays ending at that point by taking the larger of n or the sum of n and max_sum. Finally, the function returns the minimum of the two sums, which means it returns the minimum sum of any non-empty sub-array of nums. This method is efficient and avoids unnecessary complexity issues.