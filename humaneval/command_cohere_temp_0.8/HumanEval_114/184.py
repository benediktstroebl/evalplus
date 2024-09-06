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

This script provides a function that takes in one parameter, a list of integers called 'nums.' It aims to find the minimum sum of any non-empty sub-array within the given array. To do so, it initializes variables min_sum and cur_sum, the former keeping track of the minimum sum found so far, and the latter helping to calculate the sum of the current sub-array. The loop goes through each element n in 'nums,' and at the very end, returns min_sum, the minimum sum of any sub-array.

Here is a markdown code block with the same code for readability:
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

This script will correctly find the smallest sub-array sum for any list of integers provided to the function.