Here is a Python script with a self-contained function that solves the problem:
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
```
The function minSubArraySum takes in an array of integers nums and iterates through them, tracking two variables cur_sum and min_sum. cur_sum keeps track of the sum of the current subarray, initialized to the first element of nums. The min_sum variable keeps track of the minimum value encountered so far, initially set to the first element of nums as well.

During each iteration of the loop, the function adds the current element n to the cur_sum variable. If cur_sum goes negative, it resets it to 0, essentially starting a new subarray sum calculation. The min_sum variable is updated if the current element n is less than the current min_sum value.

Finally, the function returns the minimum of min_sum and cur_sum. The min_sum represents the minimum sum of any non-empty sub-array of nums, and cur_sum represents the minimum sum of the current sub-array seen so far. The final result will be the lesser of these two values.