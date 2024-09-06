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

This script provides a function called `minSubArraySum` that takes in one argument, `nums`, which represents the array of integers. The purpose of the function is to find the minimum sum of any non-empty sub-array within the given array. To achieve this, it maintains a current sum (`cur_sum`) of integers encountered so far, initializing it to the first integer in the array. It also keeps track of the minimum sum encountered (`min_sum`) thus far, initially set to the first integer in the array. The function iterates through the array, adding each integer to the current sum. If the current sum becomes negative, it resets it to zero, as a sub-array with a negative sum is not beneficial. The min_sum variable is updated accordingly whenever a smaller sum (cur_sum) is encountered. Finally, the function returns the min_sum, which represents the minimum sum of any non-empty sub-array in the input array.