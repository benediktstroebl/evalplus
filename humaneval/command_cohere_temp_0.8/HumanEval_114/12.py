Here's a Python function that solves the problem you've outlined, along with a markdown code block showing the complete script including automated tests:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return max(max_sum, min_sum, -max_sum-1)

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
nums2 = [-1, -2, -3]

assert minSubArraySum(nums1) == 1
assert minSubArraySum(nums2) == -6

```
This script includes two test cases that validate the function's behavior against the examples provided in the problem statement.