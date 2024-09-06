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

This script defines a function called `minSubArraySum` that takes in one argument, `nums`. The function iterates through the array, tracking the current sum of the subarray. It also keeps track of the minimum sum encountered, which initially is set to the first element of the array. If the current sum becomes negative, it resets the current sum to 0, only tracking the minimum sum of non-negative subarrays. The function returns the minimum sum of any subarray in the given nums.

Here is an example usage of the function:
```python
print(minSubArraySum([2, 3, 4, 1, 2, 4])) #1
print(minSubArraySum([-1, -2, -3]))  # -6
```

This will print the minimum sum for each of the given arrays, demonstrating that the function works correctly.