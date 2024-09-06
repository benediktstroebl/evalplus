Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in an array of integers nums and finds the minimum sum of any sub-array within *nums*. It does so by maintaining a cur_sum variable, which is the sum of seen elements so far, and a min_sum variable, which is the minimum sum encountered so far. As it iterates through *nums*, it keeps track of the maximum sum possible and updates *min_sum* whenever necessary. Ultimately, *min_sum* will contain the minimum sum of any sub-array in *nums*.

This approach takes advantage of the fact that the minimum sub-array sum can be identified by computing a cumulative sum of the elements, while keeping track of the minimum cumulative sum encountered, which proves effective for both positive and negative integer inputs.