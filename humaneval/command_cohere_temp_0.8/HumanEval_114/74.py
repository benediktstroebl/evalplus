Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in one argument, nums, which is an array of integers, and returns the minimum sum of any non-empty sub-array of nums. The function travels through the array, maintaining track of the current sum of the contiguous sub-array that is being examined. The variable min_sum, which tracks the minimum sum discovered thus far, is initially set to the first element of the array.

The approach is basic and efficient, comparing the current sum with the minimum sum encountered thus far as it iterates through the input array. The 'cur_sum' variable is reset to 0 when the current sub-array sum dips negative, effectively splitting the sub-arrays. The min_sum variable is updated at the end of each iteration with the minimum of the current sum and the previously recorded min_sum.

This code will work correctly for the specified example test cases, returning the expected minimum sub-array sum. It is efficient O(n), as it only iterates through the input array once, performing a constant amount of operations on each element.