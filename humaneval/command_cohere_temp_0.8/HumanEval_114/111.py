```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return min(max_sum, max(nums)) - min_sum
```
The minSubArraySum Python function uses dynamic programming to efficiently compute the minimum sum of any non-empty sub-array within the input array nums. Here's how the code works:
1. The function starts with two variables, min_sum and max_sum, both initialized with the value of the first element of the input array, nums[0].
2. It then iterates through each element, n, in the nums array. 
3. In each iteration, it updates max_sum considering two cases: 
- max_sum + n, which represents the maximum sum of sub-arrays ending at the current element.
- n, which considers the current element as a potential element of the sub-array sum.
4. It only updates min_sum with the current element, n, representing the minimum sum of sub-arrays ending at the current element. 
5. After iterating through all elements, it calculates the final result as the minimum of two values: max_sum and the maximum element in the input array nums. The max_sum value is subtracted from the result of the final result to ensure the minimum sub-array sum is correctly calculated. 

The result is a single integer, the minimum sum of any non-empty sub-array within the input nums array. This approach is dynamic programming, where you maintain two useful sums to efficiently compute the result, making it optimal with respect to time and space complexity.