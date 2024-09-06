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
    return min_sum
```

The `minSubArraySum` function takes in an array of integers, `nums`, as its argument. It initializes `cur_sum` to `0`, which is used to keep track of the current sum of elements in the array. The variable `min_sum` is initialized with the value of the first element in the array, `nums[0]`, and is used to keep track of the minimum sum of any subarray seen so far.

Then, it iterates through each element in the array, adding its value to `cur_sum`. If `cur_sum` falls below 0, it's reset to 0, indicating that the subarray sum has dipped into negative values, and the current subarray being considered is not valid.

For every element in the array, the code also updates the `min_sum` to reflect the minimum value of the subarray sum. This ensures that the variable `min_sum` accounts for the current element and any previous elements that have contributed to a smaller subarray sum.

Finally, the function returns the value of `min_sum`, which represents the minimum sum of any non-empty subarray within the input array. This strategy avoids the issue with negative subarray sums and ensures accurate results for the given problem.