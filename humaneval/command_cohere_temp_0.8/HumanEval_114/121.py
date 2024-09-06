Here's a Python function that solves the problem you've outlined, with a markdown code block containing the Python code:
```python
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = current_sum + num
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)
    
    return min(min_sum, max_sum)
```

This function employs three variables: `min_sum`, `max_sum`, and `current_sum`. Initially, `current_sum` is set to the first element of the array `nums`. As the function iterates through the array, `current_sum` is updated to reflect the sum of the current element and all previous elements. The `min_sum` and `max_sum` variables are also updated accordingly, in each iteration, to track the minimum and maximum value of `current_sum` throughout the journey. Finally, the function returns the minimum of either `min_sum` or `max_sum`, guaranteeing the minimum subarray sum.  This approach provides a time complexity of `O(n)` with an efficient constant space complexity, due to the use of only a few variable variables.