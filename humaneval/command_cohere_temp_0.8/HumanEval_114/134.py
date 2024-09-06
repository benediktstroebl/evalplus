Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for num in nums:
        cur_sum += num
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in an array of integers nums and finds the minimum sum of any sub-array within **'nums'**. It does so by maintaining a cur_sum variable, which represents the sum of the current contiguous sub-array being examined. The function resets cur_sum to 0 whenever it becomes negative, indicating the start of a new sub-array. The minimum sum encountered among these sub-arrays is kept in the min_sum variable, initialized to infinity, and is returned once all sub-arrays are examined.